
from django.urls import path
from accounts.views import RegisterView,CustomTokenObtainPairView,LogoutView,UserProfileView
from rest_framework_simplejwt.views import TokenRefreshView


app_name = "accounts"


urlpatterns = [
         path('register/', RegisterView.as_view(), name='register'),
         path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
         path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
         path('logout/', LogoutView.as_view(), name='logout'),
         path('profile/', UserProfileView.as_view(), name='user-profile'),
]