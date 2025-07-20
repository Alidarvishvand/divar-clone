from django.urls import path
from .views import PostCreateView, ApprovedPostListView,PostDetailView,PostListAPIView


app_name = "blog"


urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('list/', ApprovedPostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/', PostListAPIView.as_view(), name='post-list'),
]