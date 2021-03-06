# Generated by Django 3.0.3 on 2020-08-03 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_map', '0005_auto_20200803_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visiting_day', models.DateField()),
                ('comment', models.CharField(max_length=500)),
                ('grade', models.IntegerField(max_length=5)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant_map.Restaurant')),
            ],
        ),
    ]
