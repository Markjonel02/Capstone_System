# Generated by Django 4.1.3 on 2023-05-02 01:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesTransaction', '0065_alter_transaction_installment_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='installment_due',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 1, 1, 41, 1, 498464)),
        ),
    ]
