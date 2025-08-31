from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','author','text','created_at','lat','lon','visibility')
        read_only_fields = ('author','created_at')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','post','commenter','text','created_at')
        read_only_fields = ('commenter','created_at')