from django.contrib import admin
from GiftWithCause_DjangoProject.gift_searches.models import GiftSearch


@admin.register(GiftSearch)
class GiftSearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'up_to_price', 'user')
