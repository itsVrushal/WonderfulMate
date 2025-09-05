from django.urls import path, include
from django.contrib import admin
from django.http import HttpResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def home(request):
    return HttpResponse("Welcome to WonderfulMate API")

urlpatterns = [
    # JWT authentication endpoints
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', home),  # <-- root path

    # Your app URLs
    path('api/users/', include('apps.users.urls')),
    path('api/posts/', include('apps.posts.urls')),
    path('api/interactions/', include('apps.interactions.urls')),
    path('api/matching/', include('apps.matching.urls')),
]
