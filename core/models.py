from django.db import models
from django.contrib.auth.models import AbstractUser
import hashlib
import random
import uuid
# Create your models here.


class RollCall(models.Model):
    started = models.DateTimeField(auto_now=True)
    closed = models.BooleanField(default=False)

class CallIn(models.Model):
    rollcall =  models.ForeignKey('RollCall', related_name='callin', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', related_name='callin', on_delete=models.CASCADE)

class Person(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)