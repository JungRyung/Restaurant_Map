from django.db import models

# Create your models here.

# python manage.py makemigrations
# python manage.py migrate

class RestaurantList(models.Model):
	name = models.TextField(max_length=50)
	address = models.TextField(max_length=100)
