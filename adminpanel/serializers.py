from rest_framework import serializers
from blog.models import Post
from accounts.models import CustomUser
from category.models import Category
from adminpanel.models import Report, AdminSupportMessage, SystemConfig, AdminActionLog



class AdminPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'phone', 'first_name', 'last_name', 'is_active', 'is_staff']

class AdminCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'





class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = [
            'id',
            'report_type',
            'message',
            'reason',
            'reporter',
            'reported_post',
            'reported_user',
            'created_at',
            'is_resolved',
        ]
        read_only_fields = ['id', 'created_at', 'is_resolved']


    
        def create(self, validated_data):
            validated_data['reporter'] = self.context['request'].user
            return super().create(validated_data)

class AdminSupportMessageSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source="user.email", read_only=True)
    class Meta:
        model = AdminSupportMessage
        fields = ["id", "user", "user_email", "subject", "message", "is_answered", "created_at"]
        read_only_fields = ["created_at"]


class SystemConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemConfig
        fields = ["id", "key", "value"]


class AdminActionLogSerializer(serializers.ModelSerializer):
    admin_user_email = serializers.CharField(source="admin_user.email", read_only=True)

    class Meta:
        model = AdminActionLog
        fields = ["id", "admin_user_email", "action", "created_at"]