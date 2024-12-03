from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GiftWithCause_DjangoProject.common.urls')),
    path('', include('GiftWithCause_DjangoProject.accounts.urls')),
    path('gifts/', include('GiftWithCause_DjangoProject.gifts.urls')),
    path('gift-searches/', include('GiftWithCause_DjangoProject.gift_searches.urls')),
    path('our-heroes/', include('GiftWithCause_DjangoProject.gift_creators.urls')),
]
