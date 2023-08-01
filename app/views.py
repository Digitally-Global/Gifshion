from django.db.models import SlugField
from django.shortcuts import render, redirect
from ecom.models import *
from app.BlueDart import *
from app.mail import EmailThread,WelcomeThread,OtpThread
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import razorpay
import csv
from ecom.models import size as Size
from django.contrib.auth.decorators import login_required
from colorfield.fields import ColorField
from ecom.models import CartItem 
from paypalrestsdk import Payment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ecom.models import Wishlist
from ecom.models import Profile as pf
from django.conf import settings
from ecom.models import Currency
from ecom.models import Payment as PayModel
from django.views.generic import ListView
from .forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
import json
from random import randint
from .get_rate import *
import random

client = razorpay.Client(auth=("rzp_test_G54HO1qwPxfLIK", "nsmyogYOo15yxx4LpqtfEzMG"))

@login_required(login_url="/myaccount/login/")
def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'checkout/order_detail.html', {'order': order})

@login_required(login_url="/myaccount/login/")
def single_checkout(request,id):
    cart = CartItem.objects.filter(user=request.user)
    cart.delete()
    product = Product.objects.get(id=id)
    cart_add(request,product.id)
    return redirect('checkout')
    

def mail(request,email):
    Mail.objects.create(email=email,user=request.user)
    return redirect('Home')
@login_required(login_url="/myaccount/login/")
def wishlist(request):
    if request.method == 'POST':
        product_id = request.POST.get('id')
        action = request.POST.get('action')
        product = Product.objects.get(id=int(product_id))
        print(product,product_id)
        if product_id and action:
            print(product)
            if action == 'add':
                    wishlist_items = Wishlist.objects.filter(user=request.user,product=product)
                    if len(wishlist_items) > 0:
                        return redirect('wishlist')
                    Wishlist.objects.create(user=request.user, product=product)
            elif action == 'remove':
                Wishlist.objects.filter(user=request.user, product=product).delete()
            return redirect('wishlist')
    else:
        wishlist_items = Wishlist.objects.filter(user=request.user)
        context = {'wishlist_items': wishlist_items}
        return render(request, 'wishlist/wishlist.html', context)

@login_required(login_url="/myaccount/login/")
class OrderListView(ListView):
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-order_date')
    template_name = 'Payment/order_list.html' 
    
    
def switch_currency(request, id):
    currency=Currency.objects.get(id=id)
    print("Cuurency",currency.code)
    request.session['currency_code'] = currency.code
    request.session['exchange']=float(currency.exchange_rate)
    request.session["icon"]=currency.icon
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url="/myaccount/login/")
def cash_confrim(request):
    if request.method == "POST":
        if not request.POST.get('check'):
            req_otp = json.loads(request.body.decode("utf-8"))["otp"]
            if int(req_otp) == int(request.session['otp']):
                return JsonResponse({'status': 'true'})
            else:
                return JsonResponse({'status': 'false'})
        else:
            otp = request.POST.get('opt')
            if int(otp) == int(request.session['otp']):
                order = Order()
                order.user = request.user
                total  = request.session['cart_total_amount']
                checkout = Checkout.objects.get(id=request.session['checkout_id'])
                if checkout.coupons:
                    discounted_price = checkout.coupons.get_discounted_value(initial_value=total)
                else:
                    discounted_price = total
                total=round(total,2)
                discounted_price=round(discounted_price,2)
                order.total_amount = round(discounted_price)
                order.currency = 'INR'
                order.save()
                cart = CartItem.objects.filter(user=request.user)
                for value in cart:
                    item = OrderItem()
                    item.order = order
                    item.product = Product.objects.get(id=value.product.id)
                    item.product.save()
                    item.quantity = value.quantity
                    item.price = str(round(float(value.price)/request.session['exchange'],2))
                    item.color = value.color
                    item.size = value.size
                    item.thumbnail = value.product.image
                    if item.size and item.color: 
                        for stock in item.product.product_stock_set.all():
                            if stock.Color == item.color and stock.Size == item.size:
                                stock.stock -= item.quantity
                                stock.save()
                    elif item.size:
                        for stock in item.product.product_stock_set.all():
                            if stock.Size == item.size:
                                stock.stock -= item.quantity
                                stock.save()
                    elif item.color:
                        for stock in item.product.product_stock_set.all():
                            print('Stock',stock)
                            if stock.Color == item.color:
                                stock.stock -= item.quantity
                                stock.save()
                    else:
                        item.product.stock -= item.quantity
                        item.product.save()
                    item.save()
                order.checkout=Checkout.objects.get(id=request.session['checkout_id'])
                order.paid = False
                order.save()
                client = BlueDart(order,order.checkout,request.user)
                response = client.create_waybill()
                _payment = PayModel()
                _payment.paymentId = order.id
                _payment.payment_method = "Cash On Delevery"
                _payment.order = order
                _payment.data = json.dumps(request.POST)
                _payment.save()
                EmailThread(order,Currency.objects.get(code=order.currency).icon).start()
                cart=CartItem.objects.filter(user=request.user)
                cart.delete()
                request.session.pop('checkout_id')
                return redirect('successful')
            else:
                return render(request, "payment_failed.html")

@login_required(login_url="/myaccount/login/")
def Cash(request):
    if not request.POST.get('otp'):
        otp = randint(100000, 999999) 
    else:
        otp = request.POST.get('otp')
    request.session['otp'] = otp
    OtpThread(request.user,otp).start()
    return render(request, 'Payment/cash.html')

@csrf_exempt
@login_required(login_url="/myaccount/login/")
def confirm_razor_payment(request):
    def verify_signature(response_data):
        return client.utility.verify_payment_signature(response_data)
    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")   
        order = Order()
        order.razorpay_order_id = provider_order_id
        order.user = request.user
        total  = request.session['cart_total_amount']
        checkout = Checkout.objects.get(id=request.session['checkout_id'])
        if checkout.coupons:
            discounted_price = checkout.coupons.get_discounted_value(initial_value=total)
        else:
            discounted_price = total
        total=round(total,2)
        discounted_price=round(discounted_price,2)
        order.total_amount = round(discounted_price)
        order.currency = 'INR'
        order.save()
        cart = CartItem.objects.filter(user=request.user)
        for value in cart:
            item = OrderItem()
            item.order = order
            item.product = Product.objects.get(id=value.product.id)
            item.product.save()
            item.quantity = value.quantity
            item.price = str(round(float(value.price)/request.session['exchange'],2))
            item.color = value.color
            item.size = value.size
            item.thumbnail = value.product.image
            if item.size and item.color: 
                for stock in item.product.product_stock_set.all():
                    if stock.Color == item.color and stock.Size == item.size:
                        stock.stock -= item.quantity
                        stock.save()
            elif item.size:
                for stock in item.product.product_stock_set.all():
                    if stock.Size == item.size:
                        stock.stock -= item.quantity
                        stock.save()
            elif item.color:
                for stock in item.product.product_stock_set.all():
                    print('Stock',stock)
                    if stock.Color == item.color:
                        stock.stock -= item.quantity
                        stock.save()
            else:
                item.product.stock -= item.quantity
                item.product.save()
            item.save()
        order.checkout=Checkout.objects.get(id=request.session['checkout_id'])
        order.save()
        _payment = PayModel()
        _payment.paymentId = payment_id
        _payment.payment_method = "RazorPay"
        _payment.order = order
        _payment.data = json.dumps(request.POST)
        _payment.save()
        if verify_signature(request.POST):
            order.paid = True
            order.save()
            EmailThread(order,Currency.objects.get(code=order.currency).icon).start()
            client = BlueDart(order,order.checkout,request.user)
            client.create_waybill()
            cart=CartItem.objects.filter(user=request.user)
            cart.delete()
            return redirect('successful')
        else:
            return render(request, "payment_failed.html")
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = Order.objects.get(razorpay_order_id=provider_order_id)
        _payment = PayModel()
        _payment.paymentId = payment_id
        _payment.payment_method = "RazorPay"
        _payment.order = order
        _payment.data = json.dumps(request.POST)
        order.save()
        _payment.save()
        return render(request, "payment_failed.html")

@login_required(login_url="/myaccount/login/")
def confirm_order(request):
    if request.GET.get('paymentId') and request.GET["token"] and  request.GET["PayerID"]:
        payment = Payment.find(request.GET['paymentId'])
        if payment.execute({"payer_id": request.GET["PayerID"]}):
            print("Payment[%s] execute successfully" % (payment.id))
            order = Order()
            order.user = request.user
            order.total_amount = payment.transactions[0].amount.total
            order.currency = request.session['currency_code']
            order.save()
            cart = CartItem.objects.filter(user=request.user)
            for value in cart:
                item = OrderItem()
                item.order = order
                item.product = Product.objects.get(id=value.product.id)
                item.quantity = value.quantity
                item.color = value.color
                item.thumbnail = value.product.image
                item.size = value.size
                item.price = str(round(float(value.price)/request.session['exchange'],2))
                print(item.color,item.size,"Hello Woerls ")
                if item.size and item.color: 
                    for stock in item.product.product_stock_set.all():
                        if stock.Color == item.color and stock.Size == item.size:
                            stock.stock -= item.quantity
                            stock.save()
                elif item.size:
                    for stock in item.product.product_stock_set.all():
                        if stock.Size == item.size:
                            stock.stock -= item.quantity
                            stock.save()
                elif item.color:
                    for stock in item.product.product_stock_set.all():
                        print('Stock',stock)
                        if stock.Color == item.color:
                            stock.stock -= item.quantity
                            stock.save()
                else:
                    item.product.stock -= item.quantity
                item.product.save()
            item.save()
            item.save()
            order.paid=True 
            order.checkout=Checkout.objects.get(id=request.session['checkout_id'])
            order.save()
            # PayModel.objects.create(paymentId=request.GET['paymentId'],data=payment,order=order,payment_method="Paypal")
            pay = PayModel()
            pay.paymentId=request.GET["paymentId"]
            pay.data = str(payment)
            pay.order=order
            pay.payment_method="Paypal"
            pay.save()
            EmailThread(order,Currency.objects.get(code=order.currency).icon).start()
            cart.delete()
            return redirect('successful')

@login_required(login_url="/myaccount/login/")
def confirm_order_payment(request):
    if request.method == 'GET' and request.GET.get('paymentId') and request.GET["token"] and  request.GET["PayerID"]:
        payment = Payment.find(request.GET['paymentId'])
        total = payment.transactions[0].amount.total
        return render(request, 'Payment/confirm.html',{'total_after_discount':total})

@login_required(login_url="/myaccount/login/")
def create_payment(request,id):
    checkout = Checkout.objects.get(id=id)
    request.session['checkout_id']=checkout.id
    cart = CartItem.objects.filter(user=request.user)
    total  = request.session['cart_total_amount']
    print(total)
    if checkout.coupons:
        discounted_price = checkout.coupons.get_discounted_value(initial_value=total)
    else:
        discounted_price = total
    total=round(total,2)
    discounted_price=round(discounted_price,2)
    print(total,discounted_price)
    data = []
    weights = 0
    if len(cart) == 0:
        return redirect('cart')
    for value in cart:
        sub_data = {}
        sub_data['name'] = value.product.name
        sub_data['quantity'] = value.quantity
        sub_data['price'] = str(round(float(value.price)/request.session['exchange'],2))
        weights += float(value.size.weight)*value.quantity
        sub_data['quantity']=value.quantity
        sub_data['currency']=request.session['currency_code']
        data.append(sub_data)
    if request.session['currency_code'] == 'INR':
        DATA = {
            "amount": round(discounted_price)*100,
            "currency": "INR",
        }
        response = client.order.create(data=DATA)
        return render(request,'Payment/razor-pay-confirm.html',{'response':response,'total_after_discount':round(DATA["amount"]/100)})
    else:
        if checkout.coupons:
            data.append(
                {
                "name": "Coupon Code Applied",
                "quantity": "1",
                "price": f"-{round(total-discounted_price,2)}",
                "sku": "product",
                "currency": request.session['currency_code']
                }
            )   
        print("Weight"+str(weights))
        shipping_cost = getRate(checkout.country,weights)
        shipping_cost = round(shipping_cost/request.session['exchange'],2)
        print("Shipping"+str(shipping_cost))
        data.append(
            {
            "name": "Shipping Cost",
            "quantity": "1",
            "price": f"{shipping_cost}",
            "sku": "product",
            "currency": request.session['currency_code']
            }
        )
        payment = Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [{
                "amount": {
                    "total": round(discounted_price+shipping_cost,2),
                    "currency": request.session['currency_code'],
                },
                "description": "Payment for Gifsion Products",
                "item_list": {
                    "items": data
                }
            }],
            "redirect_urls": {
                "cancel_url": request.build_absolute_uri(reverse ('checkout')),
                "return_url": request.build_absolute_uri(reverse ('confirm-paypal-order')),
            }
            })
        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    return redirect(link.href)
        else:
            print(payment.error)

def share_product(request, product_id):
    product_url = request.build_absolute_uri(reverse('product_detail', args=[product_id]))
    return JsonResponse({'product_url': product_url})

@login_required(login_url="/myaccount/login/")
def cart_add(request, id):
    if not request.GET.get('color'): 
        color = None
    else:
        color = Color.objects.get(color=str((request.GET['color']).upper()))
    try:
        size = Size.objects.get(Num=request.GET['size'],product=Product.objects.get(id=id))
    except:
        size = Size.objects.filter(product=Product.objects.get(id=id))[0]
    product = Product.objects.get(id=id)
    if color and size:
        if CartItem.objects.filter(user=request.user, product=product,color=color,size=size).exists():
            cart = CartItem.objects.get(user=request.user, product=product)
            cart.quantity += 1
            cart.save()
        else:
            CartItem.objects.create(user=request.user, product=product,quantity=1,price=round(product.price-(product.Discount/100)*product.price,2),discount=product.Discount,color=color,size=size)
        return redirect("cart_detail")
    elif color:
        if CartItem.objects.filter(user=request.user, product=product,color=color).exists():
            cart = CartItem.objects.get(user=request.user, product=product)
            cart.quantity += 1
            cart.save()
        else:
            CartItem.objects.create(user=request.user, product=product,quantity=1,price=round(product.price-(product.Discount/100)*product.price,2),discount=product.Discount,color=color)
        return redirect("cart_detail")
    else:
        if CartItem.objects.filter(user=request.user, product=product,size=size).exists():
            cart = CartItem.objects.get(user=request.user, product=product)
            cart.quantity += 1
            cart.save()
        else:
            CartItem.objects.create(user=request.user, product=product,quantity=1,price=round(product.price-(product.Discount/100)*product.price,2),discount=product.Discount,size=size)
        return redirect("cart_detail")
        


@login_required(login_url="/myaccount/login/")
def item_clear(request, id):
    product = Product.objects.get(id=id)
    color = None
    size = Size.objects.filter(product=product)[0]
    if request.GET.get('color') != "": 
        color = Color.objects.get(color=str((request.GET['color']).upper()),product=product)
    if request.GET.get('size') != "" and request.GET.get('size') != "None": 
        size = Size.objects.get(Num=request.GET['size'],product=product)
    if color and size:
        cart = CartItem.objects.get(user=request.user, product=product,color=color,size=size)
    elif color:
        cart = CartItem.objects.get(user=request.user, product=product,color=color)
    elif size:
        cart = CartItem.objects.get(user=request.user, product=product,size=size)
    else:
        cart = CartItem.objects.get(user=request.user, product=product)
    cart.delete()
    return redirect("cart_detail")


@login_required(login_url="/myaccount/login/")
def item_increment(request, id):
    product = Product.objects.get(id=id)
    color = None
    size = Size.objects.filter(product=product)[0]
    if request.GET.get('color') != "": 
        color = Color.objects.get(color=str((request.GET['color']).upper()),product=product)
    if request.GET.get('size') != "" and request.GET.get('size') != "None": 
        size = Size.objects.get(Num=request.GET['size'],product=product)
    if color and size:
        cart = CartItem.objects.get(user=request.user, product=product,color=color,size=size)
    elif color:
        cart = CartItem.objects.get(user=request.user, product=product,color=color)
    elif size:
        cart = CartItem.objects.get(user=request.user, product=product,size=size)
    else:
        cart = CartItem.objects.get(user=request.user, product=product)
    cart.quantity += 1
    cart.save()
    return redirect("cart_detail")

@login_required(login_url="/myaccount/login/")
def item_decrement(request, id):
    product = Product.objects.get(id=id)
    color = None
    size = Size.objects.filter(product=product)[0]
    if request.GET.get('color') != "": 
        color = Color.objects.get(color=str((request.GET['color']).upper()),product=product)
    if request.GET.get('size') != "" and request.GET.get('size') != "None": 
        size = Size.objects.get(Num=request.GET['size'],product=product)
    if color and size:
        cart = CartItem.objects.get(user=request.user, product=product,color=color,size=size)
    elif color:
        cart = CartItem.objects.get(user=request.user, product=product,color=color)
    elif size:
        cart = CartItem.objects.get(user=request.user, product=product,size=size)
    else:
        cart = CartItem.objects.get(user=request.user, product=product)
    if cart.quantity <= 1:
        cart.delete()
    else:
        cart.quantity -= 1
        cart.save()
    return redirect("cart_detail")


@login_required(login_url="/myaccount/login/")
def cart_clear(request):
    cart = CartItem.objects.filter(user=request.user)
    for carts in cart:
        carts.delete()
    return redirect("cart_detail")

@login_required(login_url="/myaccount/login/")
def cart_detail(request):
    valid_coupon = None
    coupon = None
    Invalid_coupon = None
    if request.method =="GET":
      coupoun_code = request.GET.get('coupoun_code')
      if coupoun_code:
          try:
              coupon = Coupon_Code.sort().object.get(code = 'coupon_code')
              valid_coupon = "Are applicable on current order"
          except:
              Invalid_coupon = "Invalid"
    context = {
        'coupon': coupon,
        'valid_coupon' : valid_coupon,
        'invalid_coupon' : Invalid_coupon,
    }    
    return render(request, 'cart/cart.html',context)
def Cart(request):
        
        return render(request, 'cart/cart.html')
@login_required(login_url="/myaccount/login/")
def Pedit(request,id):
    if request.method == "POST":
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password  = request.POST.get('password')
        user = User.objects.get(id=id)
        user.username=username
        user.profile.phone=phone
        user.profile.save()
        user.email=email
        if not password=="":
            user.set_password(password)
        user.save()
        login(request,user)
        return redirect('profile')
    else:
        return render(request, "My_account/profile_edit.html")
    
def My_Account(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=username)
            user = authenticate(request, username = user.username, password = password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Invalid user and Password !')
                return redirect('login')
        except:
            messages.error(request, 'Email Does not Exist !')
            return redirect('login')
    else:
        return redirect('login')
 
def Pay(request):
    
    return render(request, 'Payment/pay.html')       

@login_required(login_url="/myaccount/login/")
def checkout(request):
    if request.method == "POST":
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        zip = request.POST.get('zip')
        city = request.POST.get('city')
        country = request.POST.get('country')
        state = request.POST.get('state')
        address = request.POST.get('address')
        checkout = Checkout(
              mobile_number = mobile_number,
                email = email,
                fname = fname,
                lname = lname,
                zip = zip,
                city = city,
                country = country,
                state = state,
                address = address,
        )
        if request.POST.get('coupon_code'):
            coupon_code = request.POST.get('coupon_code')
            if Coupon.objects.filter(code=coupon_code).exists():
                coupon = Coupon.objects.get(code=coupon_code)
                discount_value = round(coupon.get_discounted_value(initial_value=request.session.get("cart_total_amount")),2)
                checkout.coupons = coupon
            else:
                messages.error(request, "Invalid Coupon")
                return redirect("checkout")
        
        checkout.save()
        request.session['checkout_id'] = checkout.id
        if request.POST.get('type'):
            print("cash on delivery")
            print(request.session.get("checkout_id"))
            return redirect("cash_on_delivery")
        return redirect('create_payment',checkout.id)
    if request.GET.get("coupon_code"):
        if Coupon.objects.filter(code=request.GET.get("coupon_code")).exists():
            coupon = Coupon.objects.get(code=request.GET.get("coupon_code"))
            discount_value = round(coupon.get_discounted_value(initial_value=request.session.get("cart_total_amount")),2)
            coupon = {
                "code": coupon.code,
                "discount_value": discount_value,
                "discount" : round(request.session.get("cart_total_amount")-discount_value,2),
            }
            context = {
                "coupon": coupon,
            }
            messages.success(request, "Coupon Successfully Applied")
        else:
            context = {
                "coupon": {
                    "invalid": "Invalid",
                    },
            }
            messages.error(request, "Invalid Coupon Code")
    else : context = {}
    countries = []
    with open('countries.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for countr in row:
                if countr != "":
                    countries.append(countr)
    context["countries"] = countries
    return render(request, "checkout/checkout.html",context)
def filter_data(request):
    return None
def Register(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

        if User.objects.filter(username = username).exists():
            messages.error(request, 'username is already exists')
            return redirect('login')
        if User.objects.filter(email = email).exists():
            messages.error(request, 'Email is already exists')
            return redirect('login')
        user = User(
            username = username,
            email = email,
        )
        user.save()
        profile = pf.objects.create(
            user=user,
            phone=phone
        )
        user.set_password(password)
        user.save()
        login(request,user)
        WelcomeThread(user).start()
        return redirect('profile')
    else:
        return redirect('login')
    
def request_404(request):
    return render(request,'500.html')

def category_detail(request, category_id):
    Category = sub_category.objects.get(id=category_id)
    cat_ = category.objects.all()
    if len(request.GET.getlist('FilterPrice')) < 2:
        products = Product.objects.filter(sub_category=Category)
        print(products)
    else:
        filters = request.GET.getlist('FilterPrice')
        if filters[0] == "":
            filters[0] = 0
        if filters[1] == "":
            filters[1] = 1000000
        products = Product.objects.filter(sub_category=Category,price__gte=int(filters[0]),price__lte=int(filters[1]))
    return render(request, 'product/category_detail.html', { 'products': products , 'Category':cat_,'category':Category})
 
def Product_listing(request):
    try:
        search = request.GET["search"]
        search = search.strip()
        if search[-1] == "S" or search[-1] == "s":
            product = Product.objects.filter(name__icontains = search[:len(search)-2]).order_by("?")
        else:
            product = Product.objects.filter(name__icontains = search).order_by("?")
        context ={
            'product' : product,    
            'no_search':True
        }
    except:
        context = {'no_search':False }
    return render(request,'product/product-listing.html', context)
    
def Product_Detail(request, slug):
    
    product = Product.objects.filter(slug = slug)
    if product.exists():
        product = Product.objects.filter(slug = slug)
        similar_products = sub_category.objects.filter(name=product[0].sub_category.name)[0].product_set.all().exclude(slug=product[0].slug)
    else:
        return redirect('404')
   
    phone = Social.objects.all()[0].phone
    context={
        'product' : product,
        'similar_products': similar_products[:3],
        'phone_no':phone
    }
    
    return render(request,'product/product-detail.html', context)

def Home(request):
    def get_inStock(dataset):
        inStock = []
        for data in dataset:
            if int(data.stock) > 0:
                inStock.append(data)
            else:
                if data.product_stock_set.all().exists():
                    for stock in data.product_stock_set.all():
                        if int(stock.stock) > 0:
                            inStock.append(data)
                            break
        return inStock
    

            
    slider = Slider.objects.all().order_by('-id')
    banner = banner_area.objects.all().order_by('-id')[0:3]
    h1_banner = h1banner.objects.all().order_by('-id')[0:3]
    h2_banner = h2banner.objects.all().order_by('-id')[0:3]
    Category = category.objects.all().order_by('id')
    product = get_inStock(Product.objects.filter(section__name = "By Concern"))
    Rakhi =get_inStock(Product.objects.filter(section__name = "Rakhi Special"))
    BestSeller = get_inStock(Product.objects.filter(section__name="BestSeller"))
    sections = Section.objects.exclude(name="BestSeller")
    print(sections)

    context = {
        'banner' : banner,
        'slider' : slider,
        'h1_banner' : h1_banner,
        'h2_banner' : h2_banner,
        'Category' : Category,
        'Product' : product,
        'Rakhi' : Rakhi,
        'BestSeller':BestSeller,
        'sections' : sections
        }
    return render(request,'Main/home.html', context)


@login_required(login_url="/myaccount/login/")
def Profile(request):
    if request.method == "POST":
        username = request.POST.get('username')
        user = authenticate(request, username = username)
        user = User(
            username = username,
        )
        user.save()
        return redirect('profile',user)
    
    Category = category.objects.all().order_by('-id')[0:3]
    return render(request,'My_Account/profile.html')
def BASE(request):
    return render(request,'base.html')

@login_required(login_url="/myaccount/login/")
def order_page(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')  # Retrieve all orders
    # You can then loop through the orders to access individual fields
    # for order in orders:
    #     order_number = order.order_number
    #     customer_name = order.customer_name
        # ... access other fields
    # You can pass the orders queryset to the template for rendering
    return render(request, 'checkout/order_page.html', {'orders': orders})


from django.views.generic import TemplateView

@login_required(login_url="/myaccount/login/")
def PaypalReturnView(request):
    return render(request,'paypal_success.html')

@login_required(login_url="/myaccount/login/")
def PaypalCancelView(request):
    return render(request,'paypal_cancel.html')
    
@login_required(login_url="/myaccount/login/")
def paypal_process(request):
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '100.00',
        'item_name': 'Item_Name_xyz',
        'invoice': '10',
        'currency_code': 'USD',
        'notify url': request.build_absolute_uri(reverse ( 'paypal-ipn' )),
        'return': request.build_absolute_uri(reverse ('successful' )) ,
        'cancel return': request.build_absolute_uri(reverse ('checkout')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'paypal_from.html', {'form': form})

# send_mail(Order.objects.filter(id=85)[0],Currency.objects.get(code=Order.objects.filter(id=85)[0].currency).icon)

# WelcomeThread(User.objects.filter()[3]).start()

def about_us(request):
    return render(request,'Main/about-us.html')

def cancel(request):
    return render(request,'Main/cancel.html')
def exchange(request):
    return render(request,'Main/exchange.html')
def midnight_delivery(request):
    return render(request,'Main/midnight.html')

def pp(request):
    return render(request,'Main/pp.html')
def refund(request):
    return render(request,'Main/refund.html')
def tc(request):
    return render(request,'Main/tc.html')
def why_us(request):
    return render(request,'Main/why.html')

def render_register(request):
    return render(request,'registration/register.html')


from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('Home')
    
    
@login_required(login_url="/myaccount/login/")
def write_review(request,id):
    if request.method == "GET": 
        product = Product.objects.get(id=id)
        return render(request,'reviews/review.html',{"product":product})
    elif request.method == "POST":
        review = Review()
        if request.POST.get('review1') != " " and request.POST.get('rate') :
            review.description = request.POST.get('review1')
            review.rating = request.POST.get('rate')
            review.author = request.user
            review.product = Product.objects.get(id=id)
            review.save()
            return redirect(Product.objects.get(id=id).get_absolute_url())
        else:
            return redirect('write_review',id=id)