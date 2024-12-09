from django.urls import path, include

from GiftWithCause_DjangoProject.comments.views import CommentCreateView, CommentDeleteView
from GiftWithCause_DjangoProject.gifts import views


urlpatterns = [
    path('', views.GiftOffersView.as_view(), name="gift-offers"),
    path('create/', views.GiftCreateView.as_view(), name='gift-create'),
    path('<int:pk>/', include([
        path('edit/', views.GiftEditView.as_view(), name="gift-edit"),
        path('delete/', views.GiftDeleteView.as_view(), name="gift-delete"),
        path('details/', include([
            path('', views.GiftDetailView.as_view(), name="gift-details"),
            path('comments/<int:is_gift_search>/', CommentCreateView.as_view(), name="gift-comment"),
            path('comments/<int:comment_id>/delete/', CommentDeleteView.as_view(), name="gift-comment-delete"),
        ]))
    ]))
]
