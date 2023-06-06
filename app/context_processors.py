from ecom.models import *

def categories_processor(request):
  categories = sub_category.objects.all()         
  currencies = Currency.objects.all()
  social = Social.objects.all()[0]
  cart_total_amount = 0
  notification = Notification.objects.all()
  if request.user.is_authenticated:
    cart = CartItem.objects.filter(user=request.user)
    for item in CartItem.objects.filter(user=request.user):
      cart_total_amount += item.quantity * item.price
  else :
    cart = []
  return {'categories': categories,'currencies':currencies,'social':social,'cart_total_amount':cart_total_amount,'cart':cart,'notification':notification}