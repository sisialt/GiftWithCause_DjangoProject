from django.db import models


class GiftCreator(models.Model):
    user = models.OneToOneField(
        to='accounts.AppUser',
        on_delete=models.CASCADE,
    )

