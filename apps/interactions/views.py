from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Interaction, Friendship
from apps.users.models import UserProfile


class SendFriendRequest(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, to_id):
        from_profile = request.user.profile
        try:
            to_profile = UserProfile.objects.get(pk=to_id)
        except UserProfile.DoesNotExist:
            return Response({'detail':'not found'}, status=404)
        fr, created = Friendship.objects.get_or_create(from_user=from_profile, to_user=to_profile)
        return Response({'status':'ok','created':created})


class AcceptFriendRequest(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, from_id):
        try:
            fr = Friendship.objects.get(from_user__pk=from_id, to_user=request.user.profile)
        except Friendship.DoesNotExist:
            return Response({'detail':'not found'}, status=404)
        fr.status = 'accepted'
        fr.save()
        return Response({'status':'accepted'})