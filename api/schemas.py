''' List of all schemas used during the creation of entities '''

from typing import Union, List
from pydantic import BaseModel


####### Music Schemas #######

class SongDetails(BaseModel):
   title: str 
   duration: str
   artist: Union[str, None]
   lyrics: Union[str, None]
   format: Union[str, None]
   album: Union[str, None]
   genre: Union[str, None]
   link: str 

