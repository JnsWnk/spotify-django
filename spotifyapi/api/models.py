from django.db import models

class Song(models.Model):
    song_id = models.CharField(max_length=50, primary_key=True)
    song_name = models.CharField(max_length=50)
    song_artist = models.CharField(max_length=50)

    def __str__(self):
        return self.song_name