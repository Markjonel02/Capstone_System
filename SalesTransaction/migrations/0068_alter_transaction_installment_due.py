# Generated by Django 4.1.3 on 2023-05-04 00:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesTransaction', '0067_alter_transaction_installment_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='installment_due',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 0, 16, 31, 400887)),
        ),
    ]
