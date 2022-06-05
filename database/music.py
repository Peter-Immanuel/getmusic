from pymongo.database import Database
from utils.helpers import create_id
from schemas.music import Music, MusicDetails



class DBMusic:
   def __init__(self, database: Database):
      self.music = database["music"]

   def add(self, song: MusicDetails):
      print()
      print(song)
      print()
      new_id = create_id()
      self.music.update_one(
         {"id": "getMusic_", "count":{"$lt":500}}, #query to find a bucket
         {
            "$push": {"songs":song.dict()},
            "$inc": {"count":1},
            "$setOnInsert": {"id":new_id}
         },
         upsert=True
      )
      return song

   def list(self):
      pass

   def get(self):
      pass

   def update(self):
      pass

   def delete(self):
      pass
