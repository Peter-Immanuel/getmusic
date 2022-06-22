from typing import Dict, Union, List
from uuid import UUID
from fastapi import (
   APIRouter, status, 
   Depends,Query,
   status,Response
)
from fastapi.exceptions import HTTPException
from pydantic import Field
from services.music import MusicService
from schemas.music import Music
from api.schemas import SongDetails
from api.deps import get_database


router = APIRouter(prefix="/music", tags=["MUSIC"])



# list songs
@router.get("list_songs/", response_model=List[Music])
async def list_songs(
   page: int = Query(default=1, alias="page", ge=1),
   size: int = Query(default=10, alias="size", ge=10, le=500),
   title_filter: str = Query(default=None, alias="Search by title"),
   lyric_filter: str = Query(default=None, alias="Search by lyric"),
   database = Depends(get_database)
) -> List[Music]:
   try:
      songs_list = MusicService(database).list_songs(page,size)
      return songs_list
   except Exception as e:
      raise HTTPException(
         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
         detail=f"Sorry an error occured: {e}"
      )


# create songs
@router.post("/", response_model=Music)
async def create_song(music: SongDetails, database = Depends(get_database)
   ) -> Music:
   try:
      song = Music(**music.dict())
      new_music = MusicService(database).add_song(song)
      return new_music
   except Exception as e:

      raise HTTPException(
         status_code=status.HTTP_400_BAD_REQUEST,
         detail=f"Sorry an error occured: {e}"
      )


# get a specific song
@router.get("/{id}", response_model=Music)
async def get_song(id:UUID, database = Depends(get_database)) -> Music:
   try:
      song = MusicService(database).get_song(id)

      if not song:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Song not found")
      return song
   except Exception as e:
      raise HTTPException(
         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
         detail=f"Sorry an error occured: {e}"
      )


@router.put("/{id}", response_model=Music)
async def update_song(id:UUID, song:SongDetails, database=Depends(get_database)) -> Music:
   try:
      song = MusicService(database).update_song(id,song)
      return song
   except Exception as e:
      raise HTTPException(
         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
         detail=f"Sorry an error occured: {e}"
      )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_song(id:UUID, database=Depends(get_database)) -> Dict:
   try:
      MusicService(database).delete_song(id)
      return Response(status_code=status.HTTP_204_NO_CONTENT)
   except Exception as e:
      raise HTTPException(
         status_code=status.HTTP_,
         detail=f"Sorry an error occured: {e}"
      )
