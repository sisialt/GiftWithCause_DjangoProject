from django.views.generic import ListView

from GiftWithCause_DjangoProject.gift_searches.models import GiftSearch


class GiftSearchesView(ListView):
    model = GiftSearch
    template_name = 'gifts-searches.html'
    context_object_name = 'all_gifts'
    paginate_by = 1
