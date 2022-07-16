import motor.motor_asyncio
from AdityaHalder.config import *

mongo_dbb = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB_URL)
dbb = mongo_dbb["SPAMBOT"]
