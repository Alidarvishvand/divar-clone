from rest_framework import generics, permissions
from django.db.models import Q
from .models import ChatMessage
from .serializers import ChatMessageSerializer
from blog.models import Post
from django.shortcuts import get_object_or_404






class ChatListCreateView(generics.ListCreateAPIView):
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        user = self.request.user
        return ChatMessage.objects.filter(post_id=post_id).filter(
            Q(sender=user) | Q(receiver=user)
        ).order_by("timestamp")

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        sender = self.request.user

        parent_id = self.request.data.get('parent')
        if parent_id:
            parent = get_object_or_404(ChatMessage, pk=parent_id)
            receiver = parent.sender if parent.sender != sender else parent.receiver
        else:
            receiver = post.user

        serializer.save(sender=sender, receiver=receiver, post=post)

    
    
