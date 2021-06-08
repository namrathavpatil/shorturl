from django.db import models
from django.db.models.deletion import CASCADE


class Sign(models.Model):
    username = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(('password'), max_length=128)

    def __str__(self):
        return self.username


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.URLField()
    s_name = models.CharField(max_length=40)
    login = models.ForeignKey(
        Sign, on_delete=models.CASCADE, default='unknown', to_field='username')
