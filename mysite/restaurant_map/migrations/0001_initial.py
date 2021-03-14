# Generated by Django 3.1.7 on 2021-03-10 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(help_text='Restaurant ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(help_text='Comment ID', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('visiting_day', models.DateField()),
                ('comment', models.CharField(max_length=500)),
                ('grade', models.IntegerField()),
                ('restaurant_id', models.ForeignKey(db_column='restaurant_id', on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to='restaurant_map.restaurant')),
            ],
        ),
    ]
