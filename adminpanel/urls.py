from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ReportViewSet,
    SupportMessageViewSet,
    SystemConfigViewSet,
    AdminActionLogViewSet,
)

app_name = "adminpanel"

router = DefaultRouter()
router.register(r"reports", ReportViewSet, basename="report")
router.register(r"support-messages", SupportMessageViewSet, basename="support-message")
router.register(r"system-configs", SystemConfigViewSet, basename="system-config")
router.register(r"action-logs", AdminActionLogViewSet, basename="admin-log")

urlpatterns = [
    path("", include(router.urls)),
]
