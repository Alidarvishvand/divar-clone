
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet


app_name = "category"


router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = router.urls
