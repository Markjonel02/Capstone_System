# Generated by Django 4.1.3 on 2023-02-12 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerProfile', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customers',
            new_name='Customer',
        ),
    ]