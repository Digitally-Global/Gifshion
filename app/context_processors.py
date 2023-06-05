from ecom.models import *

def categories_processor(request):
 categories = sub_category.objects.all()         
 currencies = Currency.objects.all()
 social = Social.objects.all()[0]
 return {'categories': categories,'currencies':currencies,'social':social}