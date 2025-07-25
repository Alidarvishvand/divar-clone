"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from core.views import api_root

schema_view = get_schema_view(
    openapi.Info(
        title="API Blog",
        default_version="v1",
        description="API Sample",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="imalidrv@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls",namespace='accounts')),
    path("ctegory/", include("category.urls",namespace='category')),
    path("adminpanel/", include("adminpanel.urls",namespace='adminpanel')),
    path('', api_root),
    path("blog/", include("blog.urls",namespace='blog')),
    path("chat/", include("chat.urls", namespace='chat')),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "swagger/output.json/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
