from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import User

# Serializer for Django's built-in User model
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'email', 'full_name', 'role', 'avatar',
            'google_id', 'facebook_id', 'is_active', 'created_at', 'updated_at'
        ]
        required_fields = ['email', 'full_name']
        read_only_fields = ['id', 'created_at', 'updated_at']
