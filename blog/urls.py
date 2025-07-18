from django.urls import path
from .views import BlogPostListCreateView, BlogPostDetailView, CommentListCreateView, CommentDetailView

urlpatterns = [
    path('', BlogPostListCreateView.as_view(), name='home'),  # Добавлено: маршрут для корневого URL
    path('posts/', BlogPostListCreateView.as_view(), name='blogpost-list'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]