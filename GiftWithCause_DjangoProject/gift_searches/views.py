from django.views.generic import ListView
from GiftWithCause_DjangoProject.gifts.models import Gift


class GiftSearchesView(ListView):
    model = Gift
    template_name = 'gifts.html'
    context_object_name = 'all_gifts'
