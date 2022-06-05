from fastapi import (
   APIRouter, status, Depends,
   Query
)
from fastapi.exceptions import HTTPException
from services.music import MusicService
from schemas.music import MusicDetails
from api.schemas import SongDetails
from api.deps import get_database


router = APIRouter(prefix="/music", tags=["MUSIC"])


@router.post("/", response_model=MusicDetails)
async def create_music(music: SongDetails, database = Depends(get_database)):
   a = music.dict()
   b = MusicDetails(**a)
   print()
   print(a)
   print()
   print(b)
   print()
   new_music = MusicService(database).add_music(b)
   print(new_music)
   return new_music