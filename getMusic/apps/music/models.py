from uuid import uuid4
from django.db import models



class Song(models.Model):

   id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)

   title = models.CharField(max_length=150)
   engine = models.ForeignKey("Engine", on_delete=models.SET_NULL, null=True)
   playlists = models.ManyToManyField("Playlist")

   format = models.CharField(max_length=20, blank=True, null=True)
   artist = models.CharField(max_length=150, blank=True, null=True)
   duration = models.CharField(max_length=20 , blank=True, null=True)

   art = models.CharField(max_length=255, blank=True, null=True) # upload image to s3 and save title.
   lyrics = models.TextField(blank=True, null=True)
   album = models.CharField(max_length=150, blank=True, null=True)

   genre = models.CharField(max_length=100, blank=True, null=True)
   download = models.IntegerField(default=0)
    
   updated_at = models.DateTimeField(auto_now=True)
   created_at = models.DateTimeField(auto_now_add=True, editable=False)


   def __str__(self):
      return self.title


   
class Engine(models.Model):

   id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
   title = models.CharField(max_length=100)
   category = models.TextField()
   uri = models.URLField(blank=True, null=True)


   def __str__(self):
      return self.title



class Playlist(models.Model):

   id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
   title = models.CharField(max_length=200)
   songs = models.ManyToManyField(Song)
   likes = models.IntegerField(default=0)


   def __str__(self):
      return self.title
