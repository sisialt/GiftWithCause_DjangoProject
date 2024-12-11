from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView

from GiftWithCause_DjangoProject.accounts.forms import AppUserCreationForm, ProfileEditForm, CustomAuthenticationForm
from GiftWithCause_DjangoProject.accounts.models import Profile
from GiftWithCause_DjangoProject.gift_creators.models import GiftCreator
from GiftWithCause_DjangoProject.gifts.models import Gift

UserModel = get_user_model()


class AppUserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomAuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile-details', pk=request.user.pk)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile-details', pk=request.user.pk)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('profile-edit', kwargs={'pk': self.object.profile.pk})

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class AppUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserModel
    template_name = 'profile-delete.html'
    success_url = reverse_lazy('login')

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk'] or self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        user = self.get_object()  # Get the user object
        logout(request)  # Log out the user before deletion
        user.delete()  # Delete the user and any cascading data
        return redirect(self.success_url)


class ProfileDetailView(DetailView):
    model = UserModel
    template_name = 'profile-details.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return get_object_or_404(UserModel, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comments'] = self.object.comments.all()
        context['favourites'] = self.object.favourites.all()

        return context


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile-edit.html'

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user or self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        if self.request.user.is_creator:
            required_fields = ['first_name', 'last_name', 'profile_picture', 'bio']

            for field in required_fields:
                if not getattr(form.instance, field):
                    form.add_error(field, 'All fields are required for creators.')
                    return self.form_invalid(form)

        return super().form_valid(form)


class ProfilePublishedGiftsView(ListView):
    model = Gift
    template_name = 'published-gifts.html'
    context_object_name = 'published_gifts'
    paginate_by = 8

    def get_queryset(self):
        creator = get_object_or_404(GiftCreator, pk=self.kwargs['pk'])

        return Gift.objects.filter(creator=creator)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile'] = get_object_or_404(Profile, pk=self.kwargs['pk'])

        return context

