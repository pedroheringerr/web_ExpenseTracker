from django.db import models
from django.utils import timezone


# Create your models here.
class Transactions(models.Model):
    date = models.DateTimeField("Date of the transaction", default=timezone.now)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.description
