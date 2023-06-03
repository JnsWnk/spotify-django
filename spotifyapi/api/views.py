from django.contrib.auth.models import User, Group
from django.http import JsonResponse
import requests
from rest_framework import viewsets
from rest_framework import permissions
from spotifyapi.api.serializers import UserSerializer, GroupSerializer


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

def getData(request):
    # Set up Spotify API request
    url = 'https://api.spotify.com/v1/your/spotify/api/endpoint'
    headers = {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    }

    # Make the request to the Spotify API
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Failed to fetch data from Spotify API'}, status=500)
