from GiftWithCause_DjangoProject.comments.forms import CommentCreateForm
from GiftWithCause_DjangoProject.comments.models import Comment

from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from ..gift_searches.models import GiftSearch
from ..gifts.models import Gift


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk, is_gift_search, *args, **kwargs):
        if is_gift_search:
            gift = get_object_or_404(GiftSearch, pk=pk)
        else:
            gift = get_object_or_404(Gift, pk=pk)

        comment_form = CommentCreateForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)

            if is_gift_search:
                comment.to_gift_search = gift
            else:
                comment.to_gift = gift

            comment.author = request.user
            comment.save()

        return redirect(f"{request.META.get('HTTP_REFERER', '/')}#{pk}")


class CommentDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.delete()

        return redirect(f"{request.META.get('HTTP_REFERER', '/')}#{pk}")
