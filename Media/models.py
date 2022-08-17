from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Posts(models.Model):
    user = models.CharField(max_length=100)
    text = models.TextField(blank=False)
    date_created = models.DateTimeField(default=timezone.now, blank=True)
    likes = models.ManyToManyField(to=User, related_name="liked_posts")

    def __str__(self):
        return self.user


class UserSubjectsRepair(models.Model):
    math = models.CharField(max_length=200)
    english = models.CharField(max_length=200)
    physics = models.CharField(max_length=50)

    def __str__(self):
        return self.math


class UserInfoRepair(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=80)
    password = models.CharField(max_length=16)
    skills = models.ForeignKey(UserSubjectsRepair, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

