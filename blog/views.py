from rest_framework import generics, permissions
from .models import Post,PostImage
from .serializers import PostSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.views.generic.detail import DetailView


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        request_body=None,
        manual_parameters=[
            openapi.Parameter('title', openapi.IN_FORM, type=openapi.TYPE_STRING),
            openapi.Parameter('description', openapi.IN_FORM, type=openapi.TYPE_STRING),
            openapi.Parameter('price', openapi.IN_FORM, type=openapi.TYPE_INTEGER),
            openapi.Parameter('category', openapi.IN_FORM, type=openapi.TYPE_INTEGER),
            openapi.Parameter(
                'images',
                openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                required=False,
                description='Upload up to 10 images',
                collection_format='multi'
            ),
        ]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        post = serializer.save(user=self.request.user)

        images = self.request.FILES.getlist('images')
        for image in images[:10]:
            PostImage.objects.create(post=post, image=image)

        
        
class ApprovedPostListView(generics.ListAPIView):
    queryset = Post.objects.filter(is_approved=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]




class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.filter(is_approved=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    