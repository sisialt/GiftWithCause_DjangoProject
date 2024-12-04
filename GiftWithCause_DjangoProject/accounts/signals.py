from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from GiftWithCause_DjangoProject.accounts.models import Profile
from GiftWithCause_DjangoProject.gift_creators.models import GiftCreator

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile_and_creator(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

        if instance.is_creator:
            GiftCreator.objects.create(user=instance)

