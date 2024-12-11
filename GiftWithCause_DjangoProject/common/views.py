from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from GiftWithCause_DjangoProject.common.forms import SearchForm
from GiftWithCause_DjangoProject.gift_searches.models import GiftSearch
from GiftWithCause_DjangoProject.gifts.models import Gift


class HomeView(ListView):
    model = Gift
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        searched_gift = self.request.GET.get('gift', '')
        context['searched_gift'] = searched_gift

        context['search_form'] = SearchForm(self.request.GET)

        context['gift_offers'] = Gift.objects.filter(
            Q(title__icontains=searched_gift) | Q(description__icontains=searched_gift)
        ).order_by('-created_at')[:3]

        context['gift_searches'] = GiftSearch.objects.filter(
            title__icontains=searched_gift
        ).order_by('-created_at')[:3]

        return context


def about_view(request):
    return render(request, 'about.html')
