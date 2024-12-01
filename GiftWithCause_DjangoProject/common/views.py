from django.views.generic import ListView

from GiftWithCause_DjangoProject.gifts.models import Gift


# Create your views here.
class HomeView(ListView):
    model = Gift
    template_name = 'home.html'
    context_object_name = 'all_gifts'
    # paginate_by = 3
