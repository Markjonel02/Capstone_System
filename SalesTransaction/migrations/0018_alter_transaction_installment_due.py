# Generated by Django 4.2 on 2023-04-09 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesTransaction', '0017_alter_transaction_amount_alter_transaction_change_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='installment_due',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 21, 2, 38, 907978)),
        ),
    ]
