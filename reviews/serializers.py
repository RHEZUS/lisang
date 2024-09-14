from users.serializers import CustomUserSerializer
from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['user', 'rating', 'comment', 'timestamp']