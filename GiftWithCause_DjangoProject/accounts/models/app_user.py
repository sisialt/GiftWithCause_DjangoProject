from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from GiftWithCause_DjangoProject.accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_creator = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = "email"

    objects = AppUserManager()

    def __str__(self):
        return self.email
