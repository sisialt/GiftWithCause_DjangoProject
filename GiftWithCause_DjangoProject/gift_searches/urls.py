from django.urls import path, include
from GiftWithCause_DjangoProject.gift_searches import views

urlpatterns = [
    path('', views.GiftSearchesView.as_view(), name="gift-searches"),
    path('create/', views.GiftSearchCreateView.as_view(), name='gift-search-create'),
    path('<int:pk>/', include([
        path('details/', views.GiftSearchDetailView.as_view(), name="gift-search-details"),
        path('edit/', views.GiftSearchEditView.as_view(), name="gift-search-edit"),
        path('delete/', views.GiftSearchDeleteView.as_view(), name="gift-search-delete"),
    ]))
]
