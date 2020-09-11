from django.db import models

# Create your models here.

# python manage.py makemigrations
# python manage.py migrate

class Restaurant(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Comment(models.Model):
	username = models.CharField(max_length=50, default = '')
	restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
	visiting_day = models.DateField()
	comment = models.CharField(max_length=500)
	grade = models.IntegerField()

	def __str__(self):
		return self.username