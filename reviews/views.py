from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Review
from .serializers import ReviewSerializer
from events.models import Event

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdmin, IsSuperAdmin



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_review(request):
    """
    Handle POST requests to create a new Review.
    """
    event = get_object_or_404(Event, pk=request.data['event'])
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, event=event)
        #serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_review(request, pk):
    """
    Handle PUT requests to update a specific Review.
    """
    review = get_object_or_404(Review, pk=pk)
    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_review(request, pk):
    """
    Handle DELETE requests to delete a specific Review.
    """
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return Response({'message': 'Review deleted successfully!'})
