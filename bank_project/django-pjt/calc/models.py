# bank/info/models.py
from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return self.name
