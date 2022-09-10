from django.contrib.auth import get_user_model
from django.db import models


class Cookie(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256, default='')
    baker = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    ingredients = models.TextField(default="", null=True, blank=True)
    hourly_sales = models.JSONField(default=list, null=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)

    def __str__(self):
        return self.location