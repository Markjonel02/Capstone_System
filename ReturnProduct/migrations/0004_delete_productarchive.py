# Generated by Django 4.2 on 2023-04-16 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReturnProduct', '0003_alter_productarchive_date_archived'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductArchive',
        ),
    ]