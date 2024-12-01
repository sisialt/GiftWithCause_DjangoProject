from django.core import validators
from django.db import models


class GiftSearch(models.Model):
    title = models.CharField(
        max_length=150,
    )

    image = models.URLField(
        null=True,
        blank=True,
    )

    up_to_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            validators.MinValueValidator(0.0),
        ],
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        to='accounts.AppUser',
        on_delete=models.CASCADE,
        related_name='gift_searches',
    )

    def __str__(self):
        return self.title
