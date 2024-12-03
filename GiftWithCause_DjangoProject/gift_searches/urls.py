from django.urls import path
from GiftWithCause_DjangoProject.gift_searches import views

urlpatterns = [
    path('', views.GiftSearchesView.as_view(), name="gift-searches"),
]
