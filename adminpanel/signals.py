from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import Post
from accounts.models import CustomUser
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Post)
def log_post_update(sender, instance, created, **kwargs):
    if not created:
        logger.info(f"Post {instance.id} updated. Approved: {instance.is_approved}")

@receiver(post_save, sender=CustomUser)
def log_user_status_change(sender, instance, **kwargs):
    logger.info(f"User {instance.email} status changed. Active: {instance.is_active}")
