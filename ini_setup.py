from dotenv.main import load_dotenv
from pymongo import MongoClient
from dotenv import load_dotenv 
import os

load_dotenv()
con_uri = os.getenv('MongoDB_URL')
print(con_uri)

dbclient = MongoClient(con_uri)
dataB = dbclient["FreeGamesBot"]
dataCol = dataB["Servers"]
channelData = {"ServerID" : 783312544453623809 , "ChannelID" : 857178394299334676}
x = dataCol.insert_one(channelData)
print(f"Setup completed successfully for {ChannelID}")
