from database.music import DBMusic
from schemas.music import MusicDetails



class MusicService:
   def __init__(self, database):
      self.db = database


   def add_song(self, song: MusicDetails):
      new_song = DBMusic(self.db).add(song)
      return new_song

   def list_songs(self, page:int = None, size: int = None, **filter):
      songs_list = DBMusic(self.db).list()
      return songs_list