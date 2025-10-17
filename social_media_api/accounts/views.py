from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes

from .models import CustomUser
from .serializers import CustomUserSerializer, CompactUserSerializer

# AUTHENTICATION ENDPOINTS 

# ---------- USER REGISTRATION ENDPOINTS -----------

class UserRegistrationView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]



# ---------- USER LOGIN ENDPOINTS -----------

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'user': CustomUserSerializer(user).data,
                'token': token.key
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
    

# ---------- USER PROFILE MANAGEMENT ENDPOINT -----------

class UserProfileView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

# -------- USER FOLLOWERS/FOLLOWING LIST ENDPOINTS ---------

class UserFollowersView(ListCreateAPIView):
    serializer_class = CompactUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.followers.all()
    

# -------- USER FOLLOWING LIST ENDPOINTS ---------

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    """
    POST: Follow a user with given user_id
    """
    try:
        target_user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({'error' : 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if target_user == request.user:
        return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.follow(target_user)
    return Response({'status': f'You are now following {target_user.username}'}, status=status.HTTP_200_OK)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    """
    POST: Unfollow a user with given user_id
    """
    try:
        target_user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({'error' : 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if target_user == request.user:
        return Response({'error': 'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.unfollow(target_user)
    return Response({'status': f'You have unfollowed {target_user.username}'}, status=status.HTTP_200_OK)

class FollowingListView(ListCreateAPIView):
    """List of users the authenticated user is following."""
    serializer_class = CompactUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.following.all()

class FollowersListView(ListCreateAPIView):
    """List of users following the authenticated user."""
    serializer_class = CompactUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.followers.all()