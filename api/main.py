# FastAPI object is instantiated here
# Custom FastAPI configurations are done here.
from fastapi import FastAPI
from .api_v1.endpoints import music


app = FastAPI(
   title="GetMusic API service",
   description="This is the api backend service for getMusic "
)



# sub routers
app.include_router(music.router)