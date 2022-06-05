from datetime import datetime


def create_id():
   ''' 
   A function to create unique id for each bucket 
   by time instance.
   '''
   id: str = "getMusic_"
   # time = datetime.now().utcnow().timestamp()
   # id += str(time)
   return id
