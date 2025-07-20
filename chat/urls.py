from django.urls import path
from .views import ChatListCreateView


app_name = 'chat'


urlpatterns = [
    path('post/<int:post_id>/chat/', ChatListCreateView.as_view(), name="post-chat"),
]
