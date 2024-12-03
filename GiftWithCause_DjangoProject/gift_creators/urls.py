from django.urls import path

from GiftWithCause_DjangoProject.gift_creators import views

urlpatterns = [
    path('', views.GiftCreatorsView.as_view(), name="gift-creators"),
]
