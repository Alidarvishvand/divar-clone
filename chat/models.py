from django.db import models
from accounts.models import CustomUser
from blog.models import Post










class ChatMessage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="received_messages")
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    def __str__(self):
        return f"از {self.sender} به {self.receiver} در مورد {self.post.title}"

    
    def save(self, *args, **kwargs):
        if self.parent_id and not getattr(self, 'post_id', None):
            self.post = self.parent.post
        super().save(*args, **kwargs)
