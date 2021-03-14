from django.db import models

# Create your models here.

# python manage.py makemigrations
# python manage.py migrate

class Restaurant(models.Model):
	id = models.BigAutoField(help_text="Restaurant ID", primary_key=True)
	name = models.CharField(max_length=50,blank=False,null=False)
	address = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Comment(models.Model):
	id = models.BigAutoField(help_text="Comment ID", primary_key=True)
	restaurant_id = models.ForeignKey("Restaurant", related_name="restaurant", on_delete=models.CASCADE, db_column="restaurant_id")
	username = models.CharField(max_length=50,blank=False,null=False)
	visiting_day = models.DateField(blank=False,null=False)
	comment = models.CharField(max_length=500,blank=False,null=False)
	grade = models.IntegerField(blank=False,null=False)

	def __str__(self):
		return self.username