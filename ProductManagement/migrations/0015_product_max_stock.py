# Generated by Django 4.1.3 on 2023-05-01 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManagement', '0014_productarchive_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='max_stock',
            field=models.PositiveIntegerField(null=True),
        ),
    ]