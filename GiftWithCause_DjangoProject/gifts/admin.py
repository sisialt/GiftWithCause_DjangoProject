from django.contrib import admin
from GiftWithCause_DjangoProject.gifts.models import Gift


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'price', ) # add creator
