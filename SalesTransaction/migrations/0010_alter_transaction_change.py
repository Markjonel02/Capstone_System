# Generated by Django 4.1.3 on 2023-03-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesTransaction', '0009_rename_gcash_no_transaction_gcash_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='change',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]