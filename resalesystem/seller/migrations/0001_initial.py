# Generated by Django 4.1.4 on 2023-02-22 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellerRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=30)),
                ('Username', models.CharField(max_length=50, unique=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile', models.CharField(default='', max_length=10)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('Age', models.IntegerField()),
                ('Password', models.CharField(max_length=8)),
            ],
        ),
    ]
