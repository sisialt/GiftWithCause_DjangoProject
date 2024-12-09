from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GiftWithCause_DjangoProject.common.urls')),
    path('', include('GiftWithCause_DjangoProject.accounts.urls')),
    path('gifts/', include('GiftWithCause_DjangoProject.gifts.urls')),
    path('gift-searches/', include('GiftWithCause_DjangoProject.gift_searches.urls')),
    path('our-heroes/', include('GiftWithCause_DjangoProject.gift_creators.urls')),
]

handler404 = 'GiftWithCause_DjangoProject.urls.custom_404_view'
