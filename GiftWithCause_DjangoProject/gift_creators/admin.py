from django.contrib import admin

from GiftWithCause_DjangoProject.gift_creators.models import GiftCreator


@admin.register(GiftCreator)
class GiftCreatorAdmin(admin.ModelAdmin):
    pass
