from django.views.generic import ListView
from GiftWithCause_DjangoProject.gifts.models import Gift


class GiftOffersView(ListView):
    model = Gift
    template_name = 'gifts.html'
    context_object_name = 'all_gifts'
    paginate_by = 1

