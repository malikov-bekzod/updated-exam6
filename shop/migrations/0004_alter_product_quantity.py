# Generated by Django 5.0.3 on 2024-05-05 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.CharField(choices=[('kg', 'kilogram'), ('l', 'liter'), ('p', 'piece')], default='kg', max_length=40),
        ),
    ]