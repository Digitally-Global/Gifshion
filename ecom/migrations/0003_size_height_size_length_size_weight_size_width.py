# Generated by Django 4.2.2 on 2023-06-15 05:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecom", "0002_alter_product_stock"),
    ]

    operations = [
        migrations.AddField(
            model_name="size",
            name="height",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="size",
            name="length",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="size",
            name="weight",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="size",
            name="width",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]