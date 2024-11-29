from django.urls import path

from GiftWithCause_DjangoProject.common import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
]
