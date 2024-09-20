from rest_framework import serializers
from .models import Event, Category, EventImage
from reviews.models import Review
from users.serializers import CustomUserSerializer
from reviews.serializers import ReviewSerializer


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name', 'description']
        read_only_fields = ['id']

class EventSerializer(serializers.ModelSerializer):
    organizer = CustomUserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    images = EventImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'start_date', 'end_date', 'organizer', 'category', 'images', 'reviews', 'is_free', 'max_attendees']


