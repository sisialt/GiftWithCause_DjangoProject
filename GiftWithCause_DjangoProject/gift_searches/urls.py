from django.urls import path, include

from GiftWithCause_DjangoProject.comments.views import CommentCreateView, CommentDeleteView
from GiftWithCause_DjangoProject.gift_searches import views

urlpatterns = [
    path('', views.GiftSearchesView.as_view(), name="gift-searches"),
    path('create/', views.GiftSearchCreateView.as_view(), name='gift-search-create'),
    path('<int:pk>/', include([
        path('edit/', views.GiftSearchEditView.as_view(), name="gift-search-edit"),
        path('delete/', views.GiftSearchDeleteView.as_view(), name="gift-search-delete"),
        path('details/', include([
            path('', views.GiftSearchDetailView.as_view(), name="gift-search-details"),
            path('comments/<int:is_gift_search>/', CommentCreateView.as_view(), name="gift-search-comment"),
            path('comments/<int:comment_id>/delete/', CommentDeleteView.as_view(), name="gift-search-comment-delete"),
        ]))
    ]))
]
