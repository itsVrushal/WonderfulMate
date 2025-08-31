from django.urls import path, include


urlpatterns = [
path('api/auth/', include('rest_framework_simplejwt.urls')),
path('api/users/', include('apps.users.urls')),
path('api/posts/', include('apps.posts.urls')),
path('api/interactions/', include('apps.interactions.urls')),
path('api/matching/', include('apps.matching.urls')),
]