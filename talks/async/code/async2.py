import asyncio

import motor.motor_asyncio
from pymongo import ASCENDING, DESCENDING

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
db = client.clusterinfo

async def read_all():
    cursor = db.info.find().sort([("ta", ASCENDING), ])
    async for doc in cursor:
        await do_something_with(doc)
    # since 3.6 this also works:
    [doc async for doc in cursor()]
    {doc["_id"]: doc async for doc in cursor}

loop = asyncio.get_event_loop()
loop.run_until_complete(read_all())
