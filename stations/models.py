from django.db import models
from datetime import datetime


class Company(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name;


class Station(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(default=datetime.now)
    cars_capacity = models.IntegerField()
    company = models.ForeignKey('Company')

    def __str__(self):
        return self.name

    def size_description(self):
        if self.cars_capacity >= 5:
            return "Large"
        else:
            return "Small"


