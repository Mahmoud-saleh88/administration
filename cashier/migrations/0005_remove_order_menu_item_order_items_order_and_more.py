# Generated by Django 4.2.1 on 2023-05-19 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cashier', '0004_order_menu_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='menu_item',
        ),
        migrations.AddField(
            model_name='order_items',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Order_Item', to='cashier.order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order_items',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]