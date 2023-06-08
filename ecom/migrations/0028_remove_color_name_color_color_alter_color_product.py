# Generated by Django 4.0.3 on 2023-06-06 09:32

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0027_alter_checkout_coupons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='name',
        ),
        migrations.AddField(
            model_name='color',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='color',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='ecom.product'),
        ),
    ]