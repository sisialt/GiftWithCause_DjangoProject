from django.core import validators
from django.db import models
from django.utils.timezone import now


class Gift(models.Model):
    title = models.CharField(
        max_length=150,
    )

    image = models.URLField()

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            validators.MinValueValidator(0.0),
        ]
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    creator = models.ForeignKey(
        to="gift_creators.GiftCreator",
        on_delete=models.CASCADE,
        related_name='gifts',
    )

    def __str__(self):
        return self.title

