from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Category, Event
from .serializers import CategorySerializer, EventSerializer

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdmin, IsSuperAdmin

@api_view(['GET'])
#@authentication_classes([JWTAuthentication])
#@permission_classes([IsAuthenticated, IsAdmin])
def category_list(request):
    """
    Handle GET requests for Category list.
    """
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def category_create(request):
    """
    Handle POST requests to create a new Category.
    """
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def category_update(request, pk):
    """
    Handle PUT requests to update a specific Category.
    """
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def category_delete(request, pk):
    """
    Handle DELETE requests to delete a specific Category.
    """
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return Response({'message': 'User deleted successfully!'})


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def event_list(request):
    """
    Handle GET requests for Event list.
    """
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_events_by_category(request, pk):
    """
    Handle GET requests to get all events of a specific Category.
    """
    category = get_object_or_404(Category, pk=pk)
    events = category.events.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def event_detail(request, pk):
    """
    Handle GET requests to get details of a specific Event.
    """
    event = get_object_or_404(Event, pk=pk)
    serializer = EventSerializer(event)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def event_create(request):
    """
    Handle POST requests to create a new Event.
    """
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def event_update(request, pk):
    """
    Handle PUT requests to update a specific Event.
    """
    event = get_object_or_404(Event, pk=pk)
    serializer = EventSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def event_delete(request, pk):
    """
    Handle DELETE requests to delete a specific Event.
    """
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_events_by_user(request, pk):
    """
    Handle GET requests to get all events of a specific User.
    """
    events = Event.objects.filter(organizer=pk)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_events_by_date(request, date):
    """
    Handle GET requests to get all events on a specific date.
    """
    events = Event.objects.filter(date=date)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_events_by_location(request, location):
    """
    Handle GET requests to get all events in a specific location.
    """
    events = Event.objects.filter(location=location)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_events_of_the_authenticated_user(request):
    """
    Handle GET requests to get all events of the authenticated User.
    """
    events = Event.objects.filter(organizer=request.user)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)



