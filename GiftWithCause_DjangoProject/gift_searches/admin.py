from django.contrib import admin
from GiftWithCause_DjangoProject.gift_searches.models import GiftSearch


@admin.register(GiftSearch)
class GiftSearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'up_to_price', 'user', 'image', 'created_at', )
    search_fields = ('title', )
    ordering = ('-created_at', )
    list_filter = ('user', )
