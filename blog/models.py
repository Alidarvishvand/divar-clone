from django.db import models
from django.conf import settings
from category.models import Category
from accounts.models import CustomUser
# Create your models here.




class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=255,blank=False, null=False)
    province = models.CharField(max_length=50, default="تهران")
    city = models.CharField(max_length=50, default="تهران") 
    price = models.PositiveIntegerField()
    createda_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
    
    
class PostImage(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to="post_image/")
    
    
    def __str__(self):
        return f"image for {self.post.title}"
    
    