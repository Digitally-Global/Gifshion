from django.contrib import admin
from django.urls import include, path
from .import views
from django.conf import settings
from django.conf.urls.static  import static
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'wishlist'
app_name = 'cart'
app_name = 'paypalrestsdk'


urlpatterns = [
    path('404', views.request_404, name='404'),
    path('admin/', admin.site.urls),
    path('otp-confrim',views.cash_confrim,name='cash_confrim'),
    #Error
    path('checkout', views.checkout, name='checkout'),
    path('execute/<int:id>', views.create_payment, name='create_payment'),
    path('cash/', views.Cash, name='cash_on_delivery'),
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
    path('accounts/register/', views.render_register, name='register'),
    path('product/<slug:slug>', views.Product_Detail, name = 'product_detail'),
    path('product/product-listing/',views.Product_listing, name= 'product-listing'),
    path('myaccount/profile/', views.Profile, name = 'profile'),
    path("myaccount/orders", views.order_page, name="orders"),
    path("myaccount/orders/<str:id>", views.order_detail, name="order"),
    path('myaccount/login/', views.My_Account, name = 'handlemy_account'),
    path('myaccount/register/', views.Register, name = 'handleregister'),
    path('myaccount/change-currency/<int:id>' , views.switch_currency ,name="change_currency"),
    path('product/filter-data',views.filter_data,name="filter-data"),
    path('cart/cart/',views.Cart,name="cart"),
    path('mail/<str:email>',views.mail,name="mail"),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('paypal-return/', views.PaypalReturnView, name='successful'),
    path('paypal-cancel/', views.PaypalCancelView, name='cancelled'),
    path('payment', views.paypal_process, name='paypal-form'),
    path("paypal-confirm-order",views.confirm_order_payment, name="confirm-paypal-order"),
    path("confirm_order", views.confirm_order, name="confirm_order"),
    path('confirm_razor_payment',views.confirm_razor_payment, name="confirm_razor_payment"),
    path('about-us',views.about_us,name="about-us"),
    path('cancel',views.cancel,name="cancel"),
    path('why_us',views.why_us,name="why_us"),
    path('terms',views.tc,name="tc"),
    path('refund',views.refund,name="refund"),
    path('privacy_policy',views.pp,name="pp"),
    path('midnight_delivery',views.midnight_delivery,name="midnight_delivery"),
    path('exchange',views.exchange,name="exchange"),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    # path('write_review', views.write_review , name='write_review'),
 path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
 path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),





    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)