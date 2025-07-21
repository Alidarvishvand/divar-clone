from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from adminpanel.permissions import IsAdminUser
from blog.models import Post
from accounts.models import CustomUser
from category.models import Category
from adminpanel.models import Report, AdminSupportMessage, SystemConfig, AdminActionLog
from adminpanel.serializers import (
    ReportSerializer,
    AdminSupportMessageSerializer,
    SystemConfigSerializer,
    AdminActionLogSerializer,
    AdminPostSerializer, 
    AdminUserSerializer,
    AdminCategorySerializer
)



class AdminPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-createda_at')
    serializer_class = AdminPostSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        post = self.get_object()
        post.is_approved = True
        post.save()
        return Response({"message": "Post approved."})

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        post = self.get_object()
        post.is_approved = False
        post.save()
        return Response({"message": "Post rejected."})

class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-created_date')
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response({"message": "User deactivated."})

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        user = self.get_object()
        user.is_active = True
        user.save()
        return Response({"message": "User activated."})

class AdminCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = AdminCategorySerializer
    permission_classes = [IsAdminUser]




class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
    queryset = Report.objects.all()

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)


class SupportMessageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AdminSupportMessage.objects.all().order_by("-created_at")
    serializer_class = AdminSupportMessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]


class SystemConfigViewSet(viewsets.ModelViewSet):
    queryset = SystemConfig.objects.all()
    serializer_class = SystemConfigSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]


class AdminActionLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AdminActionLog.objects.all().order_by("-created_at")
    serializer_class = AdminActionLogSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]