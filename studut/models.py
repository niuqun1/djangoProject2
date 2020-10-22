from django.db import models

# Create your models here.
class Clesses(models.Model):
    title=models.CharField(max_length=21)
    m=models.ManyToManyField('Teachers')
class Teachers(models.Model):
    name=models.CharField(max_length=32)

class studet(models.Model):
    username=models.CharField(max_length=32)
    age = models.IntegerField()
    sex = models.BooleanField()
    cs=models.ForeignKey(Clesses,on_delete=models.CASCADE)
