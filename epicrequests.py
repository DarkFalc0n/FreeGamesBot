import requests
import json
import datetime
import pytz

url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
gameData = json.loads(response.text)
gameDataElements = gameData["data"]["Catalog"]["searchStore"]["elements"]

def getFreeGames():
    for x in range(len(gameDataElements)):
        y.append((gameDataElements[x]["title"]))
    return y
#Game Details = {name, company, date, active_status, image_url, game_url, og_price}
def getGameDetails(name):
    for x in range(len(gameDataElements)):
        if gameDataElements[x]["title"] == name:
            print(f"Fetched game details for {name}")
            return [gameDataElements[x]["title"], gameDataElements[x]["seller"]["name"], gameDataElements[x]["effectiveDate"][:10], gameDataElements[x]["status"], gameDataElements[x]["keyImages"][0]["url"], "https://www.epicgames.com/store/en-US/p/" + gameDataElements[x]["productSlug"], gameDataElements[x]["price"]["totalPrice"]["fmtPrice"]["origianlPrice"]]

def isOfferActive(name):
    for x in range(len(gameDataElements)):
        if gameDataElements[x]["title"] == name:
            if time.strptime(gameDataElements[x]["effectiveDate"][:10], "%d-%m-%Y") <= datetime.now(tz=utc):
                print("Detected that a  game has active offers")
                return True
            else:
                return False


