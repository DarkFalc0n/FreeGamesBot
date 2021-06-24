import pymongo

myclient = pymongo.MongoClient("mongodb+srv://FreeGamesBot:pK7XMbCvgs3VyVoo@cluster0.icvou.mongodb.net/FreeGamesBot?retryWrites=true&w=majority")
mydb = myclient["FreeGamesBot"]
mycol = mydb["Servers"]

mycol.drop()