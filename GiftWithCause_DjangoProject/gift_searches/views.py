from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from GiftWithCause_DjangoProject.comments.forms import CommentCreateForm
from GiftWithCause_DjangoProject.comments.models import Comment
from GiftWithCause_DjangoProject.gift_searches.forms import GiftSearchCreateForm, GiftSearchEditForm, \
    GiftSearchDeleteForm
from GiftWithCause_DjangoProject.gift_searches.models import GiftSearch


class GiftSearchesView(ListView):
    model = GiftSearch
    template_name = 'gifts-searches.html'
    context_object_name = 'all_gifts'
    paginate_by = 12

    def get_queryset(self):
        gifts = GiftSearch.objects.order_by('-created_at', 'title')

        return gifts


class GiftSearchCreateView(CreateView):
    model = GiftSearch
    form_class = GiftSearchCreateForm
    template_name = 'gift-search-create.html'

    def get_success_url(self):
        return reverse_lazy('gift-search-details', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        gift_search = form.save(commit=False)
        creator = self.request.user

        gift_search.user = creator
        return super().form_valid(form)


class GiftSearchDetailView(DetailView):
    model = GiftSearch
    template_name = 'gift-search-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comment_form'] = CommentCreateForm(self.request.GET)
        context['comments'] = Comment.objects.filter(to_gift_search=self.object)

        return context


class GiftSearchEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GiftSearch
    form_class = GiftSearchEditForm
    template_name = 'gift-search-edit.html'

    def get_success_url(self):
        return reverse_lazy('gift-search-details', kwargs={'pk': self.object.pk})

    def test_func(self):
        gift = get_object_or_404(GiftSearch, pk=self.kwargs['pk'])
        return self.request.user == gift.user or self.request.user.is_superuser


class GiftSearchDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = GiftSearch
    form_class = GiftSearchDeleteForm
    template_name = 'gift-search-delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        gift = get_object_or_404(GiftSearch, pk=self.kwargs['pk'])
        return self.request.user == gift.user or self.request.user.is_superuser

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
