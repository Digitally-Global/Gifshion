from ipware import get_client_ip
from .models import CartItem
from django.core import serializers
from .models import Currency
import requests 

def simplemiddleware(get_response):
    def middleware(request):
        try:
            # if request.session.get('exchange'):
            #     raise Exception("exchange rate already set")
            print(request.session["currency_code"])
            raise Exception("exchange rate already set") 
        except:
            def get_location():
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[0]
                    print("Ip"+str(ip))
                else:
                    ip = request.META.get('REMOTE_ADDR')
                    print("ip"+str(ip))
                response = requests.get(f'https://ipapi.co/{ip}/json/').json()
                return response.get("country_name")
            country = get_location()
            print("Country"+str(country))
            if country == 'India':  
                currency = Currency.objects.get(code='INR')
                request.session['currency_code'] = currency.code
                request.session['exchange']=float(currency.exchange_rate)
                request.session["icon"]=currency.icon
            elif country == 'United States':
                currency = Currency.objects.get(code='USD')
                request.session['currency_code'] = currency.code
                request.session['exchange']=float(currency.exchange_rate)
                request.session["icon"]=currency.icon
            elif country == 'United Kingdom':
                currency = Currency.objects.get(code='GBP')
                request.session['currency_code'] = currency.code
                request.session['exchange']=float(currency.exchange_rate)
                request.session["icon"]=currency.icon
            elif country == 'Australia':
                currency = Currency.objects.get(code='AUD')
                request.session['currency_code']=currency.code
                request.session['exchange']=float(currency.exchange_rate)
                request.session["icon"]=currency.icon
            else:
                currency = Currency.objects.get(code='INR')
                request.session['currency_code'] = currency.code
                request.session['exchange']=float(currency.exchange_rate)
                request.session["icon"]=currency.icon
                # details about the currency 
                # '$' for USD
                # '£' for GBP
                # '₹' for INR
                # '€' for EUR
                # for A dollar 
                # 'A$' for AUD
        response = get_response(request)
        if request.user.is_authenticated:
            request.session["cart"]=serializers.serialize('json', CartItem.objects.filter(user=request.user))
            cart_total_amount=0
            for item in CartItem.objects.filter(user=request.user):
                cart_total_amount += float(float(item.quantity) * round(float(item.price)/request.session['exchange'],2))
            request.session["cart_total_amount"]=cart_total_amount
            cart_count = 0
            for item in CartItem.objects.filter(user=request.user):
                cart_count += item.quantity 
            request.session['cart_items']=cart_count
        return response
    return middleware
