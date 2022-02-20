from django.db import models


# Create your models here.

class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    is_authenticated = True


class TradePoint(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)


class Visit(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    trade_point = models.ForeignKey(TradePoint, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
