from uuid import UUID
from pymongo.database import Database
from utils.helpers import create_id
from schemas.music import Music



class DBMusic:
   def __init__(self, database: Database):
      self.music = database["music"]

   def add(self, song: Music):
      self.music.insert_one(song.dict())
      return song

   def list(self, page: int = None, size: int = None, **filter):
      # update query if filter is present
      songs = self.music.find(filter)

      paginated_song = (
         songs.skip(size * (page-1)).limit(size)
         if (page and size) is not None else songs
      )
      return [Music(**song) for song in paginated_song]
      

   def get(self, id: UUID):
      music = self.music.find_one({"id":id})

      if music is None:
         return None
      return music    

   def update(self, id:UUID, song:Music):
      query = {"id":id}
      newvalues = {"$set": song.dict()}
      self.music.update_one(query, newvalues)
      return self.get(id)

   def delete(self, id:UUID):
      self.music.delete_one({"id":id})
      return None
