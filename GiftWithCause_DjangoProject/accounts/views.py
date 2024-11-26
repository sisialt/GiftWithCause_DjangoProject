from django.shortcuts import render
from django.views.generic import ListView

from GiftWithCause_DjangoProject.accounts.models import Profile


class HomeView(ListView):
    model = Profile
    template_name = 'my-index.html'
