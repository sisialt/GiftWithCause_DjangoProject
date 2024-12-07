from django.db.models import Q
from django.views.generic import ListView

from GiftWithCause_DjangoProject.common.forms import SearchForm
from GiftWithCause_DjangoProject.gifts.models import Gift


# Create your views here.
class HomeView(ListView):
    model = Gift
    template_name = 'home.html'
    context_object_name = 'all_gifts'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['search_form'] = SearchForm(self.request.GET)

        searched_gift = self.request.GET.get('gift', '')
        context['searched_gift'] = searched_gift

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        searched_gift = self.request.GET.get('gift')

        if searched_gift:
            queryset = queryset.filter(
                Q(title__icontains=searched_gift) | Q(description__icontains=searched_gift)
            )

        return queryset
