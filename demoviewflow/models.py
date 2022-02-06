from django.db import models
from viewflow.models import Process


class Food(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()


class Shoping(Process):
    shop_name = models.CharField(max_length=255)
    buier_name = models.CharField(max_length=255)
    foods = models.ForeignKey(Food, on_delete=False)
    approved = models.BooleanField(default=False)
