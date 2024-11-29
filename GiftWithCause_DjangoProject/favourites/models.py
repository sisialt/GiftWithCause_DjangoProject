from django.db import models


class Favourite(models.Model):
    to_gift = models.ForeignKey(
        to='gifts.Gift',
        on_delete=models.CASCADE,
        related_name='favourites',
    )

    user = models.ForeignKey(
        to='accounts.AppUser',
        on_delete=models.CASCADE,
        related_name='favourites',
    )
