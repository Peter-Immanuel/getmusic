from database.music import DBMusic
from schemas.music import MusicDetails



class MusicService:
   def __init__(self, database):
      self.db = database


   def add_music(self, song: MusicDetails):
      print(song)
      new_song = DBMusic(self.db).add(song)
      return new_song