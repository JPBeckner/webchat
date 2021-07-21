from django.db import models


class Bot(models.Model):
    name = models.CharField(max_length=10)
    url = models.CharField(max_length=100)
    command = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    __repr__ = __str__
