from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from app.mail import send_mail
from django_simple_coupons.models import Coupon
from colorfield.fields import ColorField
from shortuuid.django_fields import ShortUUIDField



class Currency(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=2)
    icon = models.CharField(max_length=5,null=True)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField()
    
    def __str__(self):
        return self.user.username

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.user.username + ' ' + self.product.name
        
class Checkout(models.Model):
    mobile_number = models.IntegerField()
    email = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    zip = models.IntegerField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    coupons = models.ForeignKey(Coupon, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.fname
class Slider(models.Model):
    image = models.ImageField(upload_to='slider_images')
    
class category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    def __str__(self):
        return self.name
# class cart(models.Model):
#     name = models.CharField(max_length=255)
#     def __str__(self):
#         return self.name
    
class main_category(models.Model):
    category  = models.ForeignKey('category', on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class sub_category(models.Model):
    main_categories =models.ForeignKey('main_category', on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    banner = models.FileField(upload_to="sub_category",blank=True)
    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Product(models.Model):
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images')
    price = models.IntegerField()
    Discount = models.IntegerField()
    Product_information = models.CharField(max_length=400)
    name = models.CharField(max_length=100)
    sub_category = models.ForeignKey(sub_category,on_delete=models.CASCADE)
    Tags = models.CharField(max_length=100)
    Description = RichTextField()
    section = models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "ecom_Product"

class Product_Stock(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Color = models.ForeignKey('Color',on_delete=models.CASCADE,null=True,blank=True)
    Size = models.ForeignKey('size',on_delete=models.CASCADE,null=True,blank=True)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.Product.name 

# make a signal to create a stock object when a new color object is create 

def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    pre_save.connect(pre_save_post_receiver, Product)
pre_save.connect(pre_save_post_receiver, Product)
class Coupon_Code(models.Model):
    code = models.CharField(max_length=100)
    discount = models.IntegerField()
    
    def __str__(self):
        return self.code
   
class Color(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="color")
    color = ColorField(default='#FF0000')
    code = models.CharField(max_length=10)
    
    def __str__(self):
        return self.code + self.product.name

class size(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Num = models.CharField(max_length=10)    
    width = models.CharField(max_length=10,null=True,blank=True)
    height = models.CharField(max_length=10,null=True,blank=True)
    length = models.CharField(max_length=10,null=True,blank=True)
    weight = models.CharField(max_length=10,null=True,blank=True)
    
    def __str__(self):
        return self.Num + self.product.name
    

class Productsimageurl(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    Image_url = models.ImageField(upload_to='product_images/')

class Additional_Information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
  
class banner_area(models.Model):
    name = models.CharField(max_length=255)
    rating= models.CharField(max_length=20)
    category= models.CharField(max_length=100)
    short_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='banner_images/')

class h1banner(models.Model):
    image = models.ImageField(upload_to='H1banner_img/')
class h2banner(models.Model):
    image = models.ImageField(upload_to='H2banner_img/')
    

class Payment(models.Model):
    paymentId = models.CharField(max_length=100,null=True)
    data = models.TextField(null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, blank=True)
    
class Tracking(models.Model):
    tracking_number = models.CharField(max_length=50)
    tracking_date = models.DateTimeField(auto_now_add=True)
    tracking_status = models.CharField(max_length=50)
    link = models.CharField(max_length=100) 
    
class Order(models.Model):
    id = ShortUUIDField(
        length=16,
        max_length=40,
        prefix="gif-",
        alphabet="abcdefg1234",
        primary_key=True,
    )
    razorpay_order_id = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    checkout = models.OneToOneField(Checkout, on_delete=models.CASCADE, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    tracking = models.OneToOneField(Tracking, on_delete=models.CASCADE, null=True, blank=True)
    ordered = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon_Code, on_delete=models.CASCADE, null=True, blank=True)
    paid = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    refund = models.BooleanField(default=False)
    currency = models.CharField(max_length=10, default='USD')
    invalid = models.BooleanField(default=False)
    
    def __str__(self):
        return f"#{self.id} on " + self.order_date.strftime("%d %b %Y")
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="products")
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True,related_name="items")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    size = models.ForeignKey(size, on_delete=models.CASCADE, null=True, blank=True)
    
def checkout(request):
    if request.method == 'POST':
        order = Order

    def __str__(self):
        return self.code    


class Social(models.Model):
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    
    def __str__(self):
        return "SOCIAL DETAILS"
    
class Mail(models.Model):
    email = models.EmailField(max_length=100,unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.email
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE,null=True)
    size = models.ForeignKey(size, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)

class Notification(models.Model):
    announcement = models.CharField(max_length=100)
    def __str__(self):
        return self.announcement
    

def mail_sender(sender, instance, *args, **kwargs):
    if instance.ordered:
        send_mail(instance)
    pre_save.connect(mail_sender, Order)
pre_save.connect(mail_sender, Order)