from dotenv.main import load_dotenv
import pymongo
from dotenv import load_dotenv 

load_dotenv
connect = os.getenv('MongoDB_URL')

def setup(x,y):
    dbclient = pymongo.MongoClient(connect)
    dataB = dbclient["FreeGamesBot"]
    dataCol = dataB["Servers"]
    channelData = {"ServerID" : x , "ChannelID" : y}
    x = dataCol.insert_one(channelData)
    print(f"Setup completed successfully for {ChannelID}")
    
