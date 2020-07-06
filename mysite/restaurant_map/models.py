from django.db import models

# Create your models here.

# python manage.py makemigrations
# python manage.py migrate

class Blog(models.Model):
	text = models.TextField()