from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.shortcuts import redirect
import requests
import spotipy
from rest_framework import viewsets
from rest_framework import permissions
from spotifyapi.api.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view
from django.conf import settings


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# Not secure, to be changed later, only for testing purposes


@api_view(['GET'])
def spotify_callback(request):
    code = request.GET.get('code')

    client_id = settings.SPOTIFY_ID
    client_secret = settings.SPOTIFY_SECRET
    # Update with your actual redirect URI
    redirect_uri = "http://localhost:8000/callback"

    sp_oauth = spotipy.SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                                    redirect_uri=redirect_uri, scope='user-read-email user-read-private')
    token_info = sp_oauth.get_access_token(code)
    token = token_info['access_token']

    # Redirect the user to the frontend with the token
    frontend_url = settings.FRONTEND_URL
    # Include the token in the query parameter
    redirect_url = f'{frontend_url}?token={token}'

    return redirect(redirect_url)
