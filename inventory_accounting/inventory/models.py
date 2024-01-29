from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    system = models.CharField(max_length=40, default=None)
    quantity = models.IntegerField()
    inv_num = models.IntegerField()
    placement = models.CharField(max_length=40, default=None)
    commissioning = models.DateField()
    depreciation = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=True)


class Comment(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
