# Generated by Django 2.1.7 on 2019-03-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0017_auto_20190323_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantaddress',
            name='latitude',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='restaurantaddress',
            name='longitude',
            field=models.CharField(max_length=200),
        ),
    ]
