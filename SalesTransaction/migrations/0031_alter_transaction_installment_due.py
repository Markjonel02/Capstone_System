# Generated by Django 4.2 on 2023-04-16 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesTransaction', '0030_transaction_order_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='installment_due',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 16, 13, 50, 15, 659456)),
        ),
    ]