from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Weapon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    atk = models.IntegerField()
    critdmg = models.FloatField()
    critrate = models.FloatField()
    description = models.TextField()


    