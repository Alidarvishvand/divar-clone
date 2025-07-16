from rest_framework import serializers
from .models import Post,PostImage
from category.models import Category
from rest_framework.reverse import reverse


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']



class PostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    image_urls = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()
    share_url = serializers.SerializerMethodField()  

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'price', 'category', 'image_urls', 'phone_number', 'share_url']

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
