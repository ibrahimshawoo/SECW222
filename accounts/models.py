from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import post_save
import datetime

# Create your models here.
from mysite1 import settings


class User1(models.Model):
    start_weight = models.IntegerField(default='')
    goal_weight = models.IntegerField(default='')
    height = models.IntegerField(default='')

    def __str__(self):
        return self.user.username


def generate_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = User1.objects.create(user=kwargs['instance'])


post_save.connect(generate_profile, sender=User)


class Goals(models.Model):
    userID = models.IntegerField(default='')
    goalID = models.IntegerField(default='')
    goalName = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=300, default='')
    startDate = models.DateField(default=datetime.date.today)
    finishDate = models.DateField(default=datetime.date)
    goalWeight = models.IntegerField(default='')
    targetCalories = models.IntegerField(default='')
