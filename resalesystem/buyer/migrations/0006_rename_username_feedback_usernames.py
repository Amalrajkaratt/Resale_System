# Generated by Django 4.1.4 on 2023-03-20 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0005_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='Username',
            new_name='Usernames',
        ),
    ]
