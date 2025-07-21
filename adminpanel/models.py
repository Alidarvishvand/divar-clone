from django.db import models
from accounts.models import CustomUser
from blog.models import Post

class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('post', 'Post'),
        ('user', 'User'),
    ]

    reporter = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reports')
    reported_user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL, related_name='reported_by')
    reported_post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.SET_NULL, related_name='reports')
    report_type = models.CharField(max_length=10, choices=REPORT_TYPE_CHOICES)
    message = models.TextField()
    reason = models.TextField(default="No reason")
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.reporter.email} reported {self.report_type}"
    
    
    
    
class AdminSupportMessage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    reply = models.TextField(blank=True, null=True)
    is_replied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    replied_at = models.DateTimeField(null=True, blank=True)
    subject = models.CharField(max_length=255, default='No subject')
    is_answered = models.BooleanField(default=False) 
    def __str__(self):
        return f"Support from {self.user.email}"








class SystemConfig(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.key} = {self.value}"







class AdminActionLog(models.Model):
    admin_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    target_model = models.CharField(max_length=100)
    target_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.admin_user.email} did {self.action} on {self.target_model}:{self.target_id}"
