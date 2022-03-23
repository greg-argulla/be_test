from django.contrib.auth import get_user_model
from rest_framework import serializers
from be_test.users.models import Keyboard, Keycap

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }

class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        fields = ['id', 'name', 'switches', 'keycap', 'created_at']
        
class KeycapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keycap
        fields = ['id', 'profile', 'material', 'created_at']