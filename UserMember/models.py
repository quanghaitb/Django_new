from django.db import models

# Create your models here.
class postReg(models.Model):
    username  = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    userID = models.CharField(max_length=25)