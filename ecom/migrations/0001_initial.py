# Generated by Django 4.2.2 on 2023-08-01 17:55

import ckeditor.fields
import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "django_simple_coupons",
            "0002_alter_allowedusersrule_id_alter_coupon_code_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="banner_area",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("rating", models.CharField(max_length=20)),
                ("category", models.CharField(max_length=100)),
                ("short_description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image", models.ImageField(upload_to="banner_images/")),
            ],
        ),
        migrations.CreateModel(
            name="category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "slug",
                    models.SlugField(blank=True, default="", max_length=500, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Checkout",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mobile_number", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=100)),
                ("fname", models.CharField(max_length=100)),
                ("lname", models.CharField(max_length=100)),
                ("zip", models.CharField(max_length=20)),
                ("city", models.CharField(max_length=50)),
                ("country", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=50)),
                (
                    "coupons",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="django_simple_coupons.coupon",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Color",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "color",
                    colorfield.fields.ColorField(
                        default="#FF0000", image_field=None, max_length=18, samples=None
                    ),
                ),
                ("code", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Coupon_Code",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=100)),
                ("discount", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("code", models.CharField(max_length=10)),
                ("exchange_rate", models.DecimalField(decimal_places=2, max_digits=10)),
                ("icon", models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="h1banner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="H1banner_img/")),
            ],
        ),
        migrations.CreateModel(
            name="h2banner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="H2banner_img/")),
            ],
        ),
        migrations.CreateModel(
            name="main_category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ecom.category"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("announcement", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefg1234",
                        length=16,
                        max_length=40,
                        prefix="gif-",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "razorpay_order_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("order_date", models.DateTimeField(auto_now_add=True, null=True)),
                ("ordered", models.BooleanField(default=False)),
                ("paid", models.BooleanField(default=False)),
                ("delivered", models.BooleanField(default=False)),
                ("cancelled", models.BooleanField(default=False)),
                ("refund", models.BooleanField(default=False)),
                ("currency", models.CharField(default="USD", max_length=10)),
                ("invalid", models.BooleanField(default=False)),
                (
                    "checkout",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecom.checkout",
                    ),
                ),
                (
                    "coupon",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecom.coupon_code",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stock", models.IntegerField(default=0)),
                ("image", models.ImageField(upload_to="product_images")),
                ("price", models.IntegerField()),
                ("Discount", models.IntegerField()),
                ("Product_information", models.CharField(max_length=400)),
                ("name", models.CharField(max_length=100)),
                ("Tags", models.CharField(max_length=100)),
                ("Description", ckeditor.fields.RichTextField()),
                (
                    "slug",
                    models.SlugField(blank=True, default="", max_length=500, null=True),
                ),
            ],
            options={
                "db_table": "ecom_Product",
            },
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Slider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="slider_images")),
            ],
        ),
        migrations.CreateModel(
            name="Social",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("facebook", models.CharField(max_length=100)),
                ("twitter", models.CharField(max_length=100)),
                ("instagram", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Tracking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tracking_number", models.TextField(null=True)),
                ("data", models.TextField(null=True)),
                ("tracking_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Wishlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecom.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Vendor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                (
                    "product",
                    models.ManyToManyField(related_name="vendor", to="ecom.product"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="sub_category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("banner", models.FileField(blank=True, upload_to="sub_category")),
                (
                    "mobile_banner",
                    models.FileField(blank=True, upload_to="sub_category"),
                ),
                ("hand_delivery", models.BooleanField(default=False)),
                (
                    "main_categories",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecom.main_category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="size",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Num", models.CharField(blank=True, max_length=10, null=True)),
                ("width", models.CharField(blank=True, max_length=10, null=True)),
                ("height", models.CharField(blank=True, max_length=10, null=True)),
                ("length", models.CharField(blank=True, max_length=10, null=True)),
                ("weight", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ecom.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Seller",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("rating", models.IntegerField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecom.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phone", models.CharField(max_length=10)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Productsimageurl",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Image_url", models.ImageField(upload_to="product_images/")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="ecom.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product_Stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stock", models.IntegerField(default=0)),
                (
                    "Color",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecom.color",
                    ),
                ),
                (
                    "Product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ecom.product"
                    ),
                ),
                (
                    "Size",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecom.size",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="section",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="ecom.section"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="seller",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="sub_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ecom.sub_category"
            ),
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("paymentId", models.CharField(max_length=100, null=True)),
                ("data", models.TextField(null=True)),
                ("payment_date", models.DateTimeField(auto_now_add=True)),
                ("payment_method", models.CharField(max_length=50)),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecom.order",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True, null=True, upload_to="product_images/"
                    ),
                ),
                (
                    "color",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecom.color",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="ecom.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="ecom.product",
                    ),
                ),
                (
                    "size",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecom.size",
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecom.vendor",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="tracking",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="ecom.tracking",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="Mail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=100, unique=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="color",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="color",
                to="ecom.product",
            ),
        ),
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("discount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "color",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecom.color",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ecom.product"
                    ),
                ),
                (
                    "size",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecom.size",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Additional_Information",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("specification", models.CharField(max_length=100)),
                ("detail", models.CharField(max_length=100)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ecom.product"
                    ),
                ),
            ],
        ),
    ]
