from django.db import models

# Create your models here.
    
class Maintenance(models.Model):
    contractor=models.CharField(max_length=50)
    work=models.CharField(max_length=50)
    timeperiod=models.CharField(max_length=50)
    expenses=models.IntegerField()

    def __str__(self):
        return self.contractor
    
class Workers(models.Model):
    worker=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    joiningdate=models.CharField(max_length=50)
    worklocation=models.CharField(max_length=50)

    def __str__(self):
        return self.worker
    
class finance(models.Model):
    project=models.CharField(max_length=50)
    budget=models.CharField(max_length=50)
    totexp=models.CharField(max_length=50)
    projloc=models.CharField(max_length=50)
    amtsac=models.CharField(max_length=50)

    def __str__(self):
        return self.project


class project(models.Model):
    name=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    distance=models.CharField(max_length=50)
    start=models.CharField(max_length=50)
    end=models.CharField(max_length=50)
    lanes=models.CharField(max_length=50)
    servroad=models.CharField(max_length=50)
    budget=models.CharField(max_length=50,null=True,default=True)
    def __str__(self):
        return self.name
    
class type(models.Model):
    Roadtype=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    distance=models.CharField(max_length=50)
    lanes=models.CharField(max_length=50)
    budget=models.CharField(max_length=50,null=True,default=True)
    def __str__(self):
        return self.Roadtype