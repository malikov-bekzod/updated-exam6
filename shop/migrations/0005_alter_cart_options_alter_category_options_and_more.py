# Generated by Django 5.0.3 on 2024-05-12 14:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_quantity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='product_category',
            options={'ordering': ['id']},
        ),
        migrations.AddIndex(
            model_name='cart',
            index=models.Index(fields=['id'], name='shop_cart_id_be1632_idx'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['id'], name='shop_catego_id_d67477_idx'),
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['id'], name='shop_countr_id_e169cc_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['id'], name='shop_produc_id_b93b7c_idx'),
        ),
        migrations.AddIndex(
            model_name='product_category',
            index=models.Index(fields=['id'], name='shop_produc_id_7a52a1_idx'),
        ),
    ]
