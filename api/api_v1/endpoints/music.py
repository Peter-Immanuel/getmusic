from typing import Union, List
from uuid import UUID
from fastapi import (
   APIRouter, status, Depends,
   Query
)
from fastapi.exceptions import HTTPException
from pydantic import Field
from services.music import MusicService
from schemas.music import MusicDetails
from api.schemas import SongDetails
from api.deps import get_database


router = APIRouter(prefix="/music", tags=["MUSIC"])


@router.post("/", response_model=MusicDetails)
async def create_song(
      music: SongDetails, 
      database = Depends(get_database)
   ) -> MusicDetails:
   song = MusicDetails(**music.dict())
   new_music = MusicService(database).add_music(song)
   print(new_music)
   return new_music


@router.get("/", response_model=List[MusicDetails])
async def list_songs(
   page: int = Query(default=1, alias="page", ge=1),
   size: int = Query(default=10, alias="size", ge=10, le=500),
   title_filter: str = Query(default=None, alias="Search by title"),
   lyric_filter: str = Query(default=None, alias="Search by lyric"),
   database = Depends(get_database)
) -> List[MusicDetails]:

   songs_list = MusicService(database).list_songs(page,size)
   return songs_list


@router.get("/{id}", response_model=MusicDetails)
async def get_song(id:UUID, database = Depends(get_database)):
   song = MusicService(database).get_song(id)

   # if not song:
   #    raise HTTPException(status_code=404, detail="Song not found")
   return song