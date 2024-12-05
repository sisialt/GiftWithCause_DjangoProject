from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class GiftCreator(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='gift_creator',
    )

    def __str__(self):
        return self.user.email

