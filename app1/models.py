from django.db import models

# Create your models here.
class Players(models.Model):
    pname=models.CharField(max_length=200)
    age=models.IntegerField()
    role=models.CharField(max_length=300)
    nationality=models.CharField(max_length=200)
    baseprice=models.IntegerField()







