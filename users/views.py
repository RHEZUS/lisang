from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdmin, IsSuperAdmin


User = get_user_model()

@api_view(['POST'])
def register_user(request):
    data = request.data
    serealizer = CustomUserSerializer(data=data)
    if not serealizer.is_valid():
        return Response({'error': serealizer.errors}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.create_user(
            full_name=data['full_name'],
            email=data['email'],
            password=data['password']
        )
        return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    # Authenticate the user
    # Assume you authenticate and generate tokens here

    user = authenticate(username=request.data['email'], password=request.data['password'])
    if user is not None:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response = Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        response.set_cookie(
            key='access_token',
            value=access_token,
            httponly=True,
            secure=False,  # Set to True in production
            samesite='Lax'
        )
        return response

    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def auth_check(request):
    return Response({'name': request.user.full_name}, status=status.HTTP_200_OK)

@api_view(['POST'])
def logout_user(request):
    response = Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
    response.delete_cookie('access_token')
    return response

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsSuperAdmin])
def get_users(request):
    users = User.objects.all()
    return Response({'users': [{'id': user.id, 'full_name': user.full_name, 'isActive': user.is_active, 'email': user.email, 'role': user.role} for user in users]})

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsSuperAdmin])
def create_user(request):
    data = request.data
    serealizer = CustomUserSerializer(data=data)
    if not serealizer.is_valid():
        return Response({'error': serealizer.errors}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create_user(
            full_name=data['full_name'],
            email=data['email'],
            password=data['password'],
            role=data['role']
        )
        return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsSuperAdmin])
def update_user(request, pk):

    #user = User.objects.get_object_or_404(pk=pk)
    user = get_object_or_404(User, pk=pk)
    data = request.data
    serializer = CustomUserSerializer(user, data=data)
    if not serializer.is_valid():
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    user.full_name=data['full_name']
    user.email=data['email']
    user.role=data['role'] if 'role' in data else user.role
    user.save()
    return Response({'message': 'User updated successfully!'})


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsSuperAdmin])
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return Response({'message': 'User deleted successfully!'})

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsSuperAdmin])
def activate_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = True
    user.save()
    return Response({'message': 'User activated successfully!'})

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsSuperAdmin])
def deactivate_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = False
    user.save()
    return Response({'message': 'User deactivated successfully!'})


@api_view(['PUT'])
def update_password(request):
    data = request.data
    user = authenticate(username=request.user.email, password=data['old_password'])
    if user is not None:
        user.set_password(data['new_password'])
        user.save()
        return Response({'message': 'Password updated successfully!'})
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
