from rest_framework import serializers
from .models import UserProfile, Telemetry
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')


class TelemetrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Telemetry
        fields = ('avg_response_time','avg_msg_length','pause_pattern')


class ProfileSerializer(serializers.ModelSerializer):
    telemetry = TelemetrySerializer()
    user = UserSerializer(read_only=True)


class Meta:
    model = UserProfile
    fields = ('user','about','interests','hobbies','lat','lon','xp','reveal_level','telemetry')

