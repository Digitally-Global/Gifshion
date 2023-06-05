from django.contrib import admin
from .models import *

class colors(admin.TabularInline):
    
    model = color
class sizes(admin.TabularInline):
    model = size
class Productsimageurls(admin.TabularInline):
    model = Productsimageurl 

class ProductAdmin(admin.ModelAdmin):
    inlines = [sizes,Productsimageurls]

admin.site.register(Product,ProductAdmin)
admin.site.register(Slider)

  

admin.site.register(category)
admin.site.register(Section)


admin.site.register(banner_area)
admin.site.register(h1banner)
admin.site.register(h2banner)
admin.site.register(sub_category)
admin.site.register(main_category)
admin.site.register(Coupon_Code)
admin.site.register(Checkout)
admin.site.register(Productsimageurl)
admin.site.register(Additional_Information)
admin.site.register(color)
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
    def has_change_permission(self, request, obj=None):
        return False
admin.site.register(Payment)
admin.site.register(Order,OrderAdmin)