from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Students(models.Model):
    name=  models.CharField(max_length=12)
    matric_no= models.CharField(max_length=13)
    account_balance= models.IntegerField()

    

class Items(models.Model):
    name=  models.CharField(max_length=12)
    price= models.CharField(max_length=13)
   

class Items_Paid(models.Model):
    student=models.ForeignKey(Students, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    
    
