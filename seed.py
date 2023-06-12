from termcolor import colored
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
import django
django.setup()
from ecom.models import *
from ecom.models import category, main_category, sub_category

CURRENCIES  = [
  {
    "name": "United States Dollar",
    "icon": "$",
    "code": "USD",
    "exchange_rate": 1.00
  },
  {
    "name": "Indian Rupee",
    "icon": "₹",
    "code": "INR",
    "exchange_rate": 74.00
  },
  {"name":"Australia Dollar",
  "icon":"$",
  "code":"AUD",
  "exchange_rate":1.00
   },
  {
    "name": "Great Britain Pound",
    "icon": "£",
    "code": "GBP",
    "exchange_rate": 0.72
  }
]

def create_admin_user():
  try:
    if len(User.objects.filter(is_superuser=True)) == 0:
      user = User()
      user.username = "admin"
      user.email = "admin@gmail.com"
      user.set_password("admin")
      user.is_superuser = True
      user.is_staff = True
      user.save()
      print(colored("[+] Admin User Created", "green"))
      print(colored("[+] Username: admin", "green"))
      print(colored("[+] Password: admin", "green"))
    else:
      print(colored("[+] Admin User Already Exists", "yellow"))
  except Exception as e:
    print(colored(f"[!] Error Creating Admin User: {e}", "red"))

def created_categories():
  try:
    if category.objects.filter(name = 'Best Seller').exists():
      print(colored("[+] Categories Already Exists", "yellow"))
    else:
      category.objects.create(
        name="Best Seller"
      )
      print(colored("[+] Categories Created", "green"))
    if main_category.objects.filter( name = 'Best Seller').exists():
      print(colored("[+] Categories Already Exists", "yellow"))
    else:
      main_category.objects.create(
        name="Best Seller",
        category = category.objects.get(name = 'Best Seller')
      )
      sub_category.objects.create(
      name="Best Seller",
      main_category = main_category.objects.get(name = 'Best Seller')
    )
    print(colored("[+] Categories Created", "green"))
  except Exception as e:
    print(colored(f"[!] Error Creating Categories: {e}", "red"))

def create_currency():
  try:
    if len(Currency.objects.filter()) == 0:
      for currency in CURRENCIES:
        _currency = Currency()
        _currency.name = currency["name"]
        _currency.icon = currency["icon"]
        _currency.code = currency["code"]
        _currency.exchange_rate = currency["exchange_rate"]
        _currency.save()
        print(colored(f"[+] Currency Created ", "green"))
      print(colored("[+] Currency Created", "green"))
    else:
      print(colored("[+] Currency Already Exists", "yellow"))
  except Exception as e:
    print(colored(f"[!] Error Creating Currency: {e}", "red"))
      

def create_social_media():
  try:
    if len(Social.objects.all()) == 0:
      social = Social()
      social.facebook = "https://www.facebook.com/"
      social.twitter = "https://twitter.com/"
      social.instagram = "https://www.instagram.com/"
      social.save()
      print(colored("[+] Social Media Created", "green"))
    else:
      print(colored("[+] Social Media Already Exists", "yellow"))
  except Exception as e:
    print(colored(f"[!] Error Creating Social Media: {e}", "red"))
    
if __name__ == "__main__":
  print(colored("[+] Starting Seeding", "green"))
  create_admin_user()
  create_currency()
  created_categories()
  create_social_media()
  print(colored("[+] Seeding Completed", "green"))