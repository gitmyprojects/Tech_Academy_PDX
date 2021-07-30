from django.db import models

class User(models.Model):
    handle = models.CharField(max_length=20,unique=True, default="")
    password = models.CharField(max_length=25, unique=True, default="")
    email = models.EmailField(max_length=254, unique=True, default="")
    points = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    users = models.Manager()

    def __str__(self):
        return self.handle
