from django.db import models

# Create your models here.
class Contractor(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    zip_code=models.IntegerField()
class Companies(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    zip_code=models.IntegerField()
class Job(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=50)
    price=models.IntegerField()
    company=models.CharField(max_length=50)
    contractor=models.CharField(max_length=50)
    date=models.DateField()
    time=models.TimeField()
