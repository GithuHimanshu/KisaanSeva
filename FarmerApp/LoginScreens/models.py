from django.db import models

# Create your models here....
class farmer(models.Model):
    Farmer_name = models.CharField(max_length = 200)
    Contact_num = models.CharField(max_length = 100)
    Email_id = models.EmailField(max_length = 200)
    Password = models.CharField(max_length = 50)

class scholar(models.Model):
    Scholar_name = models.CharField(max_length = 50)
    Contact_num = models.IntegerField(max_length = 13)
    Email_id = models.EmailField(max_length = 50)
    Password = models.CharField(max_length = 50)
