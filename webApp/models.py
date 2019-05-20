from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expence(models.Model):
    text=models.CharField(max_length=20)
    date=models.DateField()
    amount=models.BigIntegerField()
    # user=models.ForeignKey(User)
    def __str__(self):
        return "{}-{}".format(self.date,self.amount) 

class Income(models.Model):
    text=models.CharField(max_length=20)
    date=models.DateField()
    amount=models.BigIntegerField()
    def __str__(self):
       return "{}-{}".format(self.date,self.amount) 