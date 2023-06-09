# Generated by Django 4.1.4 on 2023-03-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_alter_product_email_alter_product_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_Price',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='sellerregister',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6),
        ),
    ]
