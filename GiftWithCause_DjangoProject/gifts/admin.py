from django.contrib import admin
from GiftWithCause_DjangoProject.gifts.models import Gift


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'creator', 'image', 'created_at', )
    search_fields = ('title', )
    ordering = ('-created_at', )
    list_filter = ('creator', )
