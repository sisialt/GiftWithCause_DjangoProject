from django.contrib.auth.views import LogoutView
from django.urls import path, include

from GiftWithCause_DjangoProject.accounts import views

urlpatterns = [
    path('login/', views.AppUserLoginView.as_view(), name='login'),
    path('register/', views.AppUserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('details/', views.ProfileDetailView.as_view(), name='profile-details'),
        path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', views.AppUserDeleteView.as_view(), name='profile-delete'),
        path('published-gifts/', views.ProfilePublishedGiftsView.as_view(), name='published-gifts'),
    ]))
]