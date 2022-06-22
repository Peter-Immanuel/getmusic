from uuid import UUID
from database.music import DBMusic
from schemas.music import Music



class MusicService:
   def __init__(self, database):
      self.db = database

   def add_song(self, song: Music):
      new_song = DBMusic(self.db).add(song)
      return new_song

   def list_songs(self, page:int = None, size: int = None, **filter):
      songs_list = DBMusic(self.db).list()
      return songs_list

   def get_song(self, id:UUID):
      song = DBMusic(self.db).get(id)
      if not song:
         return None
      return song

   def update_song(self, id:UUID, song:Music):
      song = DBMusic(self.db).update(id, song)
      return song

   def delete_song(self, id):
      return DBMusic(self.db).delete(id)