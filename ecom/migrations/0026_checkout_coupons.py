# Generated by Django 4.0.3 on 2023-06-06 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_coupons', '0002_alter_allowedusersrule_id_alter_coupon_code_and_more'),
        ('ecom', '0025_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='coupons',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_simple_coupons.coupon'),
        ),
    ]