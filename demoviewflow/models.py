from django.db import models
from viewflow.models import Process




class Shoping(Process):
    shop_name = models.CharField(max_length=255)
    buier_name = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)
