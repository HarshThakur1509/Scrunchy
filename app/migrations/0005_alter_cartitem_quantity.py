# Generated by Django 4.2 on 2023-06-11 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_cartitems_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
