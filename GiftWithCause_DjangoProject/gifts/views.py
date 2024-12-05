from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from GiftWithCause_DjangoProject.gifts.forms import GiftCreateForm, GiftEditForm, GiftDeleteForm
from GiftWithCause_DjangoProject.gifts.models import Gift


class GiftOffersView(ListView):
    model = Gift
    template_name = 'gifts.html'
    context_object_name = 'all_gifts'
    paginate_by = 4


class GiftCreateView(CreateView):
    model = Gift
    form_class = GiftCreateForm
    template_name = 'gift-create.html'

    def get_success_url(self):
        return reverse_lazy('gift-details', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        gift = form.save(commit=False)
        creator = self.request.user.gift_creator

        if not hasattr(creator.user, 'profile') or not creator.user.profile.first_name:
            messages.error(
                self.request,
                "You must complete your profile information before creating a gift."
            )
            return self.form_invalid(form)
            # return redirect('profile-edit', pk=self.request.user.profile.pk)

        gift.creator = creator
        return super().form_valid(form)


class GiftDetailView(DetailView):
    model = Gift
    template_name = 'gift-details.html'



