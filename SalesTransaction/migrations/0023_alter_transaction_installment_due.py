# Generated by Django 4.2 on 2023-04-10 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesTransaction', '0022_alter_installment_payment_method_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='installment_due',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 13, 29, 33, 845552)),
        ),
    ]
