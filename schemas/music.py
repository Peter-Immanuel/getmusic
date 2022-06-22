from typing import Union, List
from utils.helpers import create_id
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, HttpUrl
from .base import BaseSchema



class Music(BaseModel):
   ''' Music Entity Schema to get music from database '''
   
   id: UUID = Field(default_factory=uuid4)
   title: str 
   duration: str
   artist: Union[str, None]
   lyrics: Union[str, None]
   format: Union[str, None]
   album: Union[str, None]
   genre: Union[str, None]
   art: Union[str, None] #TODO integrate s3 bucket here to upload music image.
   link: HttpUrl
   downloads: int = Field(default=0, ge=0)



class MusicBucket(BaseSchema):
   ''' Bucket Schema pattern '''
   
   id: str = Field(default_factory=create_id)
   count: int = 0
   songs: List[Music]