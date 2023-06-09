# Generated by Django 4.2.2 on 2023-06-15 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ecom", "0003_size_height_size_length_size_weight_size_width"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="stock",
            field=models.IntegerField(default=0),
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
                        on_delete=django.db.models.deletion.CASCADE, to="ecom.color"
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
                        on_delete=django.db.models.deletion.CASCADE, to="ecom.size"
                    ),
                ),
            ],
        ),
    ]
