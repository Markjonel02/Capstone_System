# Generated by Django 4.2 on 2023-04-11 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesTransaction', '0028_alter_transaction_installment_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='installment_due',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 12, 0, 57, 7, 814218)),
        ),
    ]
