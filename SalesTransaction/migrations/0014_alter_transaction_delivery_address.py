# Generated by Django 4.2 on 2023-04-08 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesTransaction', '0013_alter_transaction_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='delivery_address',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]