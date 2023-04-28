# Generated by Django 4.2 on 2023-04-15 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesTransaction', '0029_alter_transaction_installment_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='order_type',
            field=models.CharField(blank=True, choices=[('Delivery', 'Delivery'), ('Pickup', 'Pickup')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='installment_due',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 16, 2, 58, 3, 989338)),
        ),
    ]