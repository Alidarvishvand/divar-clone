from rest_framework import serializers
from .models import ChatMessage





class ChatMessageSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        queryset=ChatMessage.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = ChatMessage
        fields = ['id', 'post', 'sender', 'receiver', 'message', 'timestamp', 'parent']
        read_only_fields = ['sender', 'receiver', 'post', 'timestamp']