from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.request import Request
from django.db.models import QuerySet
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class CreatePostView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        profile = self.request.user.profile # type: ignore
        serializer.save(author=profile)


class NearbyPostsView(generics.ListAPIView):
    serializer_class = PostSerializer       

    def get_queryset(self) -> QuerySet[Post]:   # type: ignore
        request: Request = self.request  # helps Pylance know about query_params    # type: ignore
        lat = float(request.query_params.get('lat', 0))
        lon = float(request.query_params.get('lon', 0))
        radius_km = float(request.query_params.get('radius', 50))
        return Post.objects.filter(visibility='public')


class CreateCommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        profile = self.request.user.profile# type: ignore
        serializer.save(commenter=profile)
