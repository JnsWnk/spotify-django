import spotipy
from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings

# Create a global Spotipy instance
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=settings.SPOTIFY_ID, client_secret=settings.SPOTIFY_SECRET, redirect_uri=settings.SPOTIFY_REDIRECT_URI))
