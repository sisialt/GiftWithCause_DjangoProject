from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from GiftWithCause_DjangoProject.gift_searches.forms import GiftSearchCreateForm, GiftSearchEditForm, \
    GiftSearchDeleteForm
from GiftWithCause_DjangoProject.gift_searches.models import GiftSearch


class GiftSearchesView(ListView):
    model = GiftSearch
    template_name = 'gifts-searches.html'
    context_object_name = 'all_gifts'
    paginate_by = 8

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

        # if not hasattr(creator.user, 'profile') or not creator.user.profile.first_name:
        #     messages.error(
        #         self.request,
        #         "You must complete your profile information before creating a gift."
        #     )
        #     return self.form_invalid(form)
        #     # return redirect('profile-edit', pk=self.request.user.profile.pk)

        gift_search.user = creator
        return super().form_valid(form)


class GiftSearchDetailView(DetailView):
    model = GiftSearch
    template_name = 'gift-search-details.html'


class GiftSearchEditView(UpdateView):
    model = GiftSearch
    form_class = GiftSearchEditForm
    template_name = 'gift-search-edit.html'
    success_url = reverse_lazy('gift-search-details')


class GiftSearchDeleteView(DeleteView):
    model = GiftSearch
    form_class = GiftSearchDeleteForm
    template_name = 'gift-search-delete.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
