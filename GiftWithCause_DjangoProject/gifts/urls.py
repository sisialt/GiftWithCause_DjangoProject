from django.urls import path

from GiftWithCause_DjangoProject.gifts import views

urlpatterns = [
    path('', views.GiftOffersView.as_view(), name="gift-offers"),
]
