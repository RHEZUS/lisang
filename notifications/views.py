
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Notification
from .serializers import NotificationSerializer

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdmin, IsSuperAdmin

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    """
    Handle GET requests to get all notifications.
    """
    notifications = request.user.notifications.all()
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)

#@api_view(['GET'])
#@authentication_classes([JWTAuthentication])
#@permission_classes([IsAuthenticated])
#def 