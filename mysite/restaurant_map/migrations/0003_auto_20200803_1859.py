# Generated by Django 3.0.3 on 2020-08-03 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_map', '0002_auto_20200801_2033'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RestaurantList',
            new_name='Restaurant',
        ),
    ]