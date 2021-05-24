from django.db import models


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.URLField()
    s_name = models.CharField(max_length=40)
