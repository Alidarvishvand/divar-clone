from rest_framework import serializers
from .models import Post,PostImage
from category.models import Category
from rest_framework.reverse import reverse
import os, json

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']





json_path = os.path.join(os.path.dirname(__file__), 'iran_all_provinces.json')
with open(json_path, encoding='utf-8') as f:
    iran_data = json.load(f)

PROVINCE_CHOICES = [(p['province'], p['province']) for p in iran_data]
class PostSerializer(serializers.ModelSerializer):
    province = serializers.ChoiceField(choices=PROVINCE_CHOICES)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    image_urls = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()
    share_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'description', 'price',
            'province', 
            'category', 'image_urls',
            'phone_number', 'share_url'
        ]

    def get_image_urls(self, obj):
        return [img.image.url for img in obj.images.all()]

    def get_phone_number(self, obj):
        return obj.user.phone if obj.user else None

    def get_share_url(self, obj):  
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(
                reverse('blog:post-detail', kwargs={'pk': obj.pk})
            )
        return None

    def create(self, validated_data):
        images = self.context['request'].FILES.getlist('images')
        user = validated_data.pop('user')
        post = Post.objects.create(**validated_data, user=user)
        for image in images[:10]:
            PostImage.objects.create(post=post, image=image)
        return post
