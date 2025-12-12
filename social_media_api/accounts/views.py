from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer

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


class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        if request.user.id == user_id:
            return Response({'detail': "You can't follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            target = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Add to following (directional)
        request.user.following.add(target)
        request.user.save()
        return Response({'detail': f'You are now following {target.username}.'}, status=status.HTTP_200_OK)


class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        if request.user.id == user_id:
            return Response({'detail': "You can't unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            target = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        request.user.following.remove(target)
        request.user.save()
        return Response({'detail': f'You have unfollowed {target.username}.'}, status=status.HTTP_200_OK)


class FollowingListView(APIView):
    """
    Returns the list of users the current user is following.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_qs = request.user.following.all()
        serializer = ProfileSerializer(following_qs, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowersListView(APIView):
    """
    Returns the list of users that follow the current user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        followers_qs = request.user.followers.all()
        serializer = ProfileSerializer(followers_qs, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)