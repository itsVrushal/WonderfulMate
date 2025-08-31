from rest_framework import generics, permissions
from .models import UserProfile
from .serializers import ProfileSerializer


class MeProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer


    def get_object(self):
        return self.request.user.profile  # type: ignore[attr-defined]