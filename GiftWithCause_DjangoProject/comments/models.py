from django.db import models


class Comment(models.Model):
    author = models.ForeignKey(
        to='accounts.AppUser',
        on_delete=models.CASCADE,
        related_name='comments',
    )

    text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    to_gift = models.ForeignKey(
        to='gifts.Gift',
        on_delete=models.CASCADE,
        related_name='comments',
    )

    to_gift_search = models.ForeignKey(
        to='gift_searches.GiftSearch',
        on_delete=models.CASCADE,
        related_name='comments',
    )

    def __str__(self):
        return self.text
