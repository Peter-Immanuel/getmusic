# Dependencies All Dependencies including
# database, user, active, cache etc.
 
import pymongo
from core.config import settings


def get_database():
    """
    This function returns a database conneciton for a mongodb database
    """
    client = pymongo.MongoClient(settings.DATABASE_URL, uuidRepresentation="standard")
    db = client["music-api-service"]
    return db
