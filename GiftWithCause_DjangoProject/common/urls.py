from django.urls import path

from GiftWithCause_DjangoProject.common import views
from GiftWithCause_DjangoProject.common.views import about_view

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('about/', about_view, name="about"),
]
