# Generated by Django 4.1.3 on 2023-05-01 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesTransaction', '0060_alter_transaction_installment_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='installment_due',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 18, 13, 48, 546164)),
        ),
    ]
