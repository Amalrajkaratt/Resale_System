# Generated by Django 4.1.4 on 2023-02-22 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_category_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='Mobile',
            field=models.CharField(max_length=10),
        ),
    ]
