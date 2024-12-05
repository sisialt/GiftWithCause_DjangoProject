from django.urls import path, include

from GiftWithCause_DjangoProject.gifts import views

urlpatterns = [
    path('', views.GiftOffersView.as_view(), name="gift-offers"),
    path('create/', views.GiftCreateView.as_view(), name='gift-create'),
    path('<int:pk>/', include([
        path('details/', views.GiftDetailView.as_view(), name="gift-details"),
        path('edit/', views.GiftEditView.as_view(), name="gift-edit"),
        path('delete/', views.GiftDeleteView.as_view(), name="gift-delete"),
    ]))
]
