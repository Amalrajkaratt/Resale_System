# Generated by Django 4.1.4 on 2023-03-05 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0002_addtowishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtowishlist',
            old_name='Product',
            new_name='Products',
        ),
    ]
