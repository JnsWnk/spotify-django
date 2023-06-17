from django.contrib.auth.models import User, Group
from django.http import JsonResponse
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


@api_view(['GET'])
def get_song(request):
    client_credentials_manager = spotipy.SpotifyClientCredentials(
        client_id=settings.SPOTIFY_ID, client_secret=settings.SPOTIFY_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    song = sp.search(q='track:Believe artist:Cher', type='track')

    return JsonResponse(song)
