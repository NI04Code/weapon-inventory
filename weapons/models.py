from django.db import models

# Create your models here.
class Weapon(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    atk = models.IntegerField()
    critdmg = models.FloatField()
    critrate = models.FloatField()
    description = models.TextField()