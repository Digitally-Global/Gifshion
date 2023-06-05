from django.db.models import SlugField
from django.shortcuts import render, redirect
from ecom.models import *
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from paypalrestsdk import Payment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from ecom.models import Wishlist
from ecom.models import Profile as pf
from django.conf import settings
from django.views.decorators.http import require_POST
from django.utils import timezone
from ecom.models import Currency
from ecom.models import Payment as PayModel
from django.views.generic import ListView
from .forms import PayPalPaymentsForm
from random import randint

def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'checkout/order_detail.html', {'order': order})

def single_checkout(request,id):
    cart = request.session["cart"]
    cart.clear()
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('checkout')
    
def mail(request,email):
    Mail.objects.create(email=email,user=request.user)
    return redirect(request.META.get('HTTP_REFERER'))

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

class OrderListView(ListView):
    model = Order
    template_name = 'payment/order_list.html' 
    
def switch_currency(request, id):
    currency=Currency.objects.get(id=id)
    print("Cuurency",currency.code)
    request.session['currency_code'] = currency.code
    request.session['exchange']=float(currency.exchange_rate)
    request.session["icon"]=currency.icon
    return redirect(request.META.get('HTTP_REFERER'))
   
def Cash(request):
    return render(request, 'payment/cash.html')

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
            cart = request.session['cart']
            for _,value in cart.items():
                item = OrderItem()
                item.order = order
                item.product = Product.objects.get(id=value['product_id'])
                item.quantity = value['quantity']
                item.price = str(round(float(value['price'])/request.session['exchange'],2))
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
            request.session['cart'] = {}
            return redirect('successful')

def create_payment(request):
    if request.method == 'GET' and request.GET.get('paymentId') and request.GET["token"] and  request.GET["PayerID"]:
        return render(request, 'Payment/confirm.html')
    else:
        cart = request.session['cart']
        items = len(cart)
        print(request.session['cart'])
        print(len(request.session['cart']))
        total=0
        for key,value in cart.items():
            print(key,value)
            total += round((float(value['price'])/request.session['exchange']),2)*value['quantity']
        print(str(round(total,2)))
        data = []
        for _,value in cart.items():
            sub_data = {}
            sub_data['name'] = value['name']
            sub_data['quantity'] = value['quantity']
            sub_data['price'] = str(round(float(value['price'])/request.session['exchange'],2))
            sub_data['quantity']=value['quantity']
            sub_data['currency']=request.session['currency_code']
            data.append(sub_data)   
        print(data)
        payment = Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [{
                "amount": {
                    "total":  str(round(total,2)),  # Make sure the currency amount is correctly formatted
                    "currency": request.session['currency_code'],
                },
                "description": "Payment for Gifsion Products",
                "item_list": {
                    "items": data
                }
            }],
            "redirect_urls": {
                "cancel_url": request.build_absolute_uri(reverse ('cancelled')),
                "return_url": request.build_absolute_uri(reverse ('create_payment' )),
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
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/myaccount/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/myaccount/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required(login_url="/myaccount/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/myaccount/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
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
#def Cart(request):
        
        #return render(request, 'cart/cart.html')
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
        return render(request, "my_account/profile_edit.html")
def My_Account(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Ivalid user and Password !')
            return redirect('login')
    else:
        return redirect('login')
 
def Pay(request):
    
    return render(request, 'payment/pay.html')       
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
       checkout.save()
       request.session['checkout_id'] = checkout.id
       return redirect('create_payment')
    return render(request, "checkout/checkout.html")
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
        return redirect('profile')
    else:
        return redirect('login')
    
def Error(request):
    return render(request,'Error/404.html')
def category_detail(request, category_id):
    Category = sub_category.objects.get(id=category_id)
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
    return render(request, 'product/category_detail.html', { 'products': products , 'category':Category})
 
def Product_listing(request):
    try:
        search = request.GET["search"]
        product = Product.objects.filter(name__contains = search).order_by("-id")
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
   
    context={
        'product' : product,
        'similar_products': similar_products[:3]
    }
    
    return render(request,'product/product-detail.html', context)

def Home(request):
    slider = Slider.objects.all().order_by('-id')[0:3]
    banner = banner_area.objects.all().order_by('-id')[0:3]
    h1_banner = h1banner.objects.all().order_by('-id')[0:3]
    h2_banner = h2banner.objects.all().order_by('-id')[0:3]
    Category = category.objects.all().order_by('-id')[0:3]
    product = Product.objects.filter(section__name = "By Concern")
    Rakhi = Product.objects.filter(section__name = "Rakhi Special")
    BestSeller = Product.objects.filter(section__name="Best Seller")
    Products = Product.objects.all().order_by('-id')
    sections = Section.objects.exclude(name="Best Seller")

    context = {
        'banner' : banner,
        'slider' : slider,
        'h1_banner' : h1_banner,
        'h2_banner' : h2_banner,
        'Category' : Category,
        'Product' : product,
        'Rakhi' : Rakhi,
        'BestSeller':BestSeller,
        'Products':Products,
        'sections' : sections
        }
    return render(request,'main/home.html', context)

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
    return render(request,'my_account/profile.html')
def BASE(request):
    return render(request,'base.html')

@login_required(login_url="/myaccount/login/")
def order_page(request):
    orders = Order.objects.filter(user=request.user).order_by('-id')  # Retrieve all orders
    # You can then loop through the orders to access individual fields
    # for order in orders:
    #     order_number = order.order_number
    #     customer_name = order.customer_name
        # ... access other fields
    # You can pass the orders queryset to the template for rendering
    return render(request, 'checkout/order_page.html', {'orders': orders})


from django.views.generic import TemplateView

class PaypalReturnView(TemplateView):
    template_name = 'paypal_success.html'

class PaypalCancelView(TemplateView):
    template_name = 'paypal_cancel.html'

def paypal_process(request):
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '100.00',
        'item_name': 'Item_Name_xyz',
        'invoice': '10',
        'currency_code': 'USD',
        'notify url': request.build_absolute_uri(reverse ( 'paypal-ipn' )),
        'return': request.build_absolute_uri(reverse ('successful' )) ,
        'cancel return': request.build_absolute_uri(reverse ('cancelled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'paypal_from.html', {'form': form})
