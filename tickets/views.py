from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import TicketType
from events.models import Event
from .serializers import TicketTypeSerializer

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdmin, IsSuperAdmin

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_ticket_type(request):
    """
    Handle POST requests to create a new TicketType.
    """
    event = get_object_or_404(Event, pk=request.data['event'])
    serializer = TicketTypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(event=event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_ticket_type(request, pk):
    """
    Handle PUT requests to update a specific TicketType.
    """
    ticket_type = get_object_or_404(TicketType, pk=pk)
    event = get_object_or_404(Event, pk=request.data['event'])
    serializer = TicketTypeSerializer(ticket_type, data=request.data)
    if serializer.is_valid():
        serializer.save(event=event)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_ticket_type(request, pk):
    """
    Handle DELETE requests to delete a specific TicketType.
    """
    ticket_type = get_object_or_404(TicketType, pk=pk)
    ticket_type.delete()
    return Response({'message': 'TicketType deleted successfully!'})

