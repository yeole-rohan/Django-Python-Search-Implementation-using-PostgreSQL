# Generated by Django 2.1.7 on 2019-03-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0012_auto_20190323_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantaddress',
            name='latitude',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='restaurantaddress',
            name='longitude',
            field=models.CharField(max_length=50),
        ),
    ]
