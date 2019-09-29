from django.db import models

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker

class UserStock(models.Model):
    username = models.CharField(max_length=150, primary_key=True)
    ticker = models.TextField()

    def __str__(self):
        return self.username
