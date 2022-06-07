from pymongo.database import Database
from utils.helpers import create_id
from schemas.music import Music, MusicDetails



class DBMusic:
   def __init__(self, database: Database):
      self.music = database["music"]

   def add(self, song: MusicDetails):
      db_query_exp = (
         {"id": "getMusic_", "count":{"$lt":500}}, #query to find a bucket
         {
            "$push": {"songs":song.dict()},
            "$inc": {"count":1},
            "$setOnInsert": {"id":create_id()}
         },
      )
      self.music.update_one(filter=db_query_exp[0], update=db_query_exp[1], upsert=True)
      return song

   def list(self, page: int = None, size: int = None, **filter):
      
      query = {"id":"getMusic_"}

      # update query if filter is present
      query = query.update({"song":filter.dict()}) if filter else query

      # Get buckets from database.
      query_list = self.music.find(query)

      # convert bucket data into Music Schema
      modified_query_list = [Music(**doc) for doc in query_list]   

      # extract all songs from each bucket
      songs_list = []
      for doc in modified_query_list:
         songs_list.extend(doc.songs)

      # convert songs to JSON to be consumed by frontend 
      result = [song.dict() for song in songs_list]
      return result 

      
   def get(self):
      pass

   def update(self):
      pass

   def delete(self):
      pass
