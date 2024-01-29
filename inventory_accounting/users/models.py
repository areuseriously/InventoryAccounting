from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Position(models.Model):
    name = models.CharField(max_length=100, unique=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,to_field='name', on_delete=models.CASCADE, default=True)
    position = models.ForeignKey(Position, to_field='name', on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.user.username
