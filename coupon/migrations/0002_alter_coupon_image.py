# Generated by Django 4.1.7 on 2023-03-16 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='image',
            field=models.ImageField(upload_to='uploads/coupons/'),
        ),
    ]
