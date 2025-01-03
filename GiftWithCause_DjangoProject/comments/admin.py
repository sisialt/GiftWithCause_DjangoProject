from django.contrib import admin
from GiftWithCause_DjangoProject.comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_at', 'to_gift', 'to_gift_search', )
    search_fields = ('author', )
    ordering = ('-created_at', )
    list_filter = ('author', 'to_gift', 'to_gift_search', )
