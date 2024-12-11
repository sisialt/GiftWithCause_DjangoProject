from django.views.generic import ListView
from GiftWithCause_DjangoProject.gift_creators.models import GiftCreator


class GiftCreatorsView(ListView):
    model = GiftCreator
    template_name = 'our-heroes.html'
    context_object_name = 'all_creators'
    paginate_by = 12
