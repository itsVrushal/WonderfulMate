from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # JWT authentication endpoints
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Your app URLs
    path('api/users/', include('apps.users.urls')),
    path('api/posts/', include('apps.posts.urls')),
    path('api/interactions/', include('apps.interactions.urls')),
    path('api/matching/', include('apps.matching.urls')),
]
