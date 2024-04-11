from django.db import models
from model_utils.models import TimeStampedModel, UUIDModel


class Product(UUIDModel, TimeStampedModel, models.Model):
    class CategoryChoices(models.TextChoices):
        MENS_CLOTHING = "Men's Clothing"
        WOMENS_CLOTHING = "Women's Clothing"
        ELECTRONICS = "Electronics"
        JEWELRY = "Jewellery"

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=100, choices=CategoryChoices)
    brand = models.CharField(max_length=100)
