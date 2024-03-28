from django.db import models
from model_utils.models import TimeStampedModel, UUIDModel
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(TimeStampedModel, UUIDModel, models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    # Replace with a reference to product model?
    product = models.CharField(max_length=255)
    # Replace with a reference to user model?
    user = models.CharField(max_length=255)
