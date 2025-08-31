from django.urls import path
from .views import SendFriendRequest, AcceptFriendRequest


urlpatterns = [
path('request/<int:to_id>/', SendFriendRequest.as_view(), name='send-friend-request'),
path('accept/<int:from_id>/', AcceptFriendRequest.as_view(), name='accept-friend-request'),
]