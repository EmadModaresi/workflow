from django.db import models
from river.models.fields.state import StateField


class Food2(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()


class ShopingRiver(models.Model):
    shop_name = models.CharField(max_length=255)
    buier_name = models.CharField(max_length=255)
    foods = models.ForeignKey(Food2, on_delete=models.CASCADE)
    state = StateField()