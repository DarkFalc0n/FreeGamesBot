import requests
import json

url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
gameData = json.loads(response.text)
gameDataElements = gameData["data"]["Catalog"]["searchStore"]["elements"]

for i in gameDataElements:
    ID = i["id"]
    f = open("./update_data/EGS_id.txt", "a")
    f.write(ID + "\n")