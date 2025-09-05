from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .tasks import recompute_recommendations_for_user
from apps.users.models import UserProfile


class RecommendView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        profile = request.user.profile
        # Option A: trigger recompute async and return cached if exists
        recompute_recommendations_for_user.delay(profile.id) # type: ignore
        return Response({'status':'requested', 'message':'recommendations recompute triggered'})


class SimilarityView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request, other_id):
    # Compute one-off similarity breakdown
        try:
            me = request.user.profile
            other = UserProfile.objects.get(pk=other_id)
        except UserProfile.DoesNotExist:
            return Response({'detail':'not found'}, status=404)
        # For brevity, return a placeholder
        return Response({'text_sim':0.5, 'interest_sim':0.3})