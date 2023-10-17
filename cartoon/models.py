from django.db import models

# Create your models here.
class disney(models.Model):
    channel = models.CharField(max_length=25)
    cartoon = models.CharField(max_length=25)
    character = models.CharField(max_length=25)
    time = models.TimeField()
    
    