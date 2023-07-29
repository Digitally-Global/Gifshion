from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
import datetime
from django.http.request import HttpRequest
from .models import *

class colors(admin.TabularInline):    
    model = Color
class sizes(admin.TabularInline):
    model = size
class Productsimageurls(admin.TabularInline):
    model = Productsimageurl 
    
         
class Stock_Admin(admin.TabularInline):
    model = Product_Stock
    
class ProductAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('assets/css/admin.css',)
        }
    search_fields = ['name']
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(seller=request.user)
    inlines = [sizes,Productsimageurls,colors,Stock_Admin] 

admin.site.register(Product,ProductAdmin)
admin.site.register(Slider)
admin.site.register(Review)
admin.site.register(Tracking)

  

admin.site.register(category)
admin.site.register(Section)

admin.site.register(banner_area)
admin.site.register(h1banner)
admin.site.register(h2banner)
admin.site.register(sub_category)
admin.site.register(main_category)
admin.site.register(Coupon_Code)
admin.site.register(Productsimageurl)
admin.site.register(Additional_Information)
admin.site.register(size)
admin.site.register(Currency)
admin.site.register(CartItem)
admin.site.register(Social)
admin.site.register(Mail)
admin.site.register(Wishlist)

class ItemInline(admin.StackedInline):
    model=OrderItem
class PaymentInline(admin.StackedInline):
    model = Payment
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemInline,PaymentInline]
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.order_by('-order_date')
        print(qs)
        flag=False
        for i in qs:
            for prod in i.items.all():
                if prod.product.seller == request.user:
                    flag=True
            if flag==False:
                qs = qs.exclude(id=i.id)
    
        qs = qs.order_by('-order_date')
        return qs
    def has_change_permission(self, request, obj=None):
        return False
    
class PaymentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return None
admin.site.register(Checkout,PaymentAdmin)
admin.site.register(Payment)
admin.site.register(Order,OrderAdmin)
admin.site.register(Notification)