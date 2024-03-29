# Generated by Django 4.2 on 2023-04-10 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesTransaction', '0019_alter_transaction_installment_due'),
    ]

    operations = [
        migrations.CreateModel(
            name='Installment',
            fields=[
                ('transaction_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('transaction_reference', models.IntegerField()),
                ('customer_name', models.CharField(max_length=45)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date_paid', models.DateField(auto_now=True)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Gcash', 'Gcash'), ('Banking', 'Banking')], max_length=20)),
                ('reference_no', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='transaction',
            name='installment_due',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 8, 9, 20, 760570)),
        ),
    ]
