from django.db import models
from django.db.models import Model



class model1(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class model2(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    store_id = models.ForeignKey(model1,on_delete=models.CASCADE)