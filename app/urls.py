from django.contrib import admin
from django.urls import include, path
from .import views
from django.conf import settings
from django.conf.urls.static  import static
from .views import *

app_name = 'wishlist'
app_name = 'cart'
app_name = 'paypalrestsdk'


urlpatterns = [
    path('admin/', admin.site.urls),
    #Error
    path('404', views.Error, name='404'),
    path('checkout', views.checkout, name='checkout'),
    path('execute', views.create_payment, name='create_payment'),
    path('cash/', views.Cash, name='cash'),
    path('share-product/<int:product_id>/', views.share_product, name='share_product'),
#     cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_detail/',views.cart_detail,name='cart_detail'),
    path("checkout-single/<int:id>", views.single_checkout, name="single_checkout"),
#     end cart
    path('profile_edit/<int:id>',views.Pedit,name="Pedit"),
    path('checkout/', checkout, name='checkout'),
    path('category/<int:category_id>/', category_detail, name='category'),
    path('base/', views.BASE,name='base'),
    path('', views.Home,name='Home'),
    path('wishlist/', wishlist, name='wishlist'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('product/<slug:slug>', views.Product_Detail, name = 'product_detail'),
    path('product/product-listing/',views.Product_listing, name= 'product-listing'),
    path('myaccount/profile/', views.Profile, name = 'profile'),
    path("myaccount/orders", views.order_page, name="orders"),
    path("myaccount/orders/<int:id>", views.order_detail, name="order"),
    path('myaccount/login/', views.My_Account, name = 'handlemy_account'),
    path('myaccount/register/', views.Register, name = 'handleregister'),
    path('myaccount/change-currency/<int:id>' , views.switch_currency ,name="change_currency"),
    path('product/filter-data',views.filter_data,name="filter-data"),
    path('cart/cart/',views.Cart,name="cart"),
    path('mail/<str:email>',views.mail,name="mail"),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('paypal-return/', views.PaypalReturnView.as_view(), name='successful'),
    path('paypal-cancel/', views.PaypalCancelView.as_view(), name='cancelled'),
    path('payment', views.paypal_process, name='paypal-form'),
    path("confirm_order", views.confirm_order, name="confirm_order")
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)