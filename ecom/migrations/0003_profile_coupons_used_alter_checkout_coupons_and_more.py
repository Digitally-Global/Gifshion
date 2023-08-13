# Generated by Django 4.2.2 on 2023-08-03 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "django_simple_coupons",
            "0002_alter_allowedusersrule_id_alter_coupon_code_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ecom", "0002_vendor_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="coupons_used",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="checkout",
            name="coupons",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="django_simple_coupons.coupon",
            ),
        ),
        migrations.AlterField(
            model_name="main_category",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="ecom.category",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="checkout",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="ecom.checkout",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="coupon",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="ecom.coupon_code",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="tracking",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="ecom.tracking",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="color",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="ecom.color",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="items",
                to="ecom.order",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="products",
                to="ecom.product",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="size",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="ecom.size",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="vendor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="ecom.vendor",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="seller",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="sub_category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="ecom.sub_category",
            ),
        ),
        migrations.AlterField(
            model_name="sub_category",
            name="main_categories",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="ecom.main_category",
            ),
        ),
    ]
