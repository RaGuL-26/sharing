# Generated by Django 5.0.4 on 2024-05-09 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0004_order_orderitem_order_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
