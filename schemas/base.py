from pydantic import BaseModel


class BaseSchema(BaseModel):
   schema_version: int = 1
   document_version: int = 1

'''
db.history.updateOne({ "_id": /^7000000_/, "count": { $lt: 1000 } },
    { 
    	"$push": { 
            "history": {
            	"type": "buy",
            	"ticker": "MDB",
            	"qty": 25,
            	"date": ISODate("2018-11-02T11:43:10")
    		} },
    	"$inc": { "count": 1 },
    	"$setOnInsert": { "_id": "7000000_1541184190" }
    },
    { upsert: true })

{"id": "/getMusic_/", "count":{"$lt":500}}

{
   "$push": {"songs":song.dict()},
   "$inc": {"count":1},
   "$setOnInsert": {"id":""}
}
{"upsert":True}

'''