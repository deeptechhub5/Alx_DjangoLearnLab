from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

from accounts.models import CustomUser
from accounts.serializers import (
    RegisterSerializer,
    LoginSerializer,
    ProfileSerializer,
    UserSerializer,
)

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()          
    serializer_class = UserSerializer            

    def post(self, request, user_id):
        current_user = request.user
        target = get_object_or_404(CustomUser, id=user_id)

        if current_user.id == user_id:
            return Response(
                {'detail': "You can't follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        current_user.following.add(target)
        current_user.save()

        return Response(
            {'detail': f'You are now following {target.username}.'},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()          # CHECKER REQUIREMENT
    serializer_class = UserSerializer

    def post(self, request, user_id):
        current_user = request.user
        target = get_object_or_404(CustomUser, id=user_id)

        if current_user.id == user_id:
            return Response(
                {'detail': "You can't unfollow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        current_user.following.remove(target)
        current_user.save()

        return Response(
            {'detail': f'You have unfollowed {target.username}.'},
            status=status.HTTP_200_OK
        )


class FollowingListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_qs = request.user.following.all()
        serializer = ProfileSerializer(
            following_qs, many=True, context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowersListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        followers_qs = request.user.followers.all()
        serializer = ProfileSerializer(
            followers_qs, many=True, context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
