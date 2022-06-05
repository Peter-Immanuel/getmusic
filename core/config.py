import os
from pydantic import BaseSettings


class Setting(BaseSettings):
   DATABASE_URL = DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb://localhost:27017/")



settings = Setting()