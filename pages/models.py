from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

# Create your models here.

class UserAccount(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.IntegerField(default=0)
    email = models.EmailField(max_length=254, default='n/a')
    address = models.CharField(max_length=100, default='n/a')
    city = models.CharField(max_length=25, default='n/a')
    postal = models.CharField(max_length=20, default='n/a')

    def __str__(self):
        """String for representing the Model object."""
        return str(self.first_name)

    class Meta:
        db_table ="useraccount"

     


class Area(models.Model):
    Aid=models.IntegerField(primary_key=True)
    Aname=models.CharField(max_length=200)
    class Meta:
        db_table="area"


class Restaurant(models.Model):
    Rid=models.IntegerField(primary_key=True)
    Rname=models.CharField(max_length=200)
    Aname=models.CharField(max_length=200,default='n/a')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.Rname

        

    class Meta:
        db_table="restaurant"