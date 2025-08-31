from django.urls import path
from .views import CreatePostView, NearbyPostsView, CreateCommentView


urlpatterns = [
path('', CreatePostView.as_view(), name='create-post'),
path('nearby/', NearbyPostsView.as_view(), name='nearby-posts'),
path('<int:pk>/comment/', CreateCommentView.as_view(), name='create-comment'),
]