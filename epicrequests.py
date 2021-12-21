import requests
import json
import datetime
import time
import pytz

url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"

payload={}
headers = {}

async def requestData():
    print("Fetched data now")
    response = requests.request("GET", url, headers=headers, data=payload)
    gameData = json.loads(response.text)
    global gameDataElements
    gameDataElements = gameData["data"]["Catalog"]["searchStore"]["elements"]

def getGameReleaseDate(x):
    gameReleaseDate = gameDataElements[x]["promotions"]["promotionalOffers"][0]["promotionalOffers"][0]["startDate"][:10] if gameDataElements[x]["promotions"]["promotionalOffers"] != [] else gameDataElements[x]["effectiveDate"][:10]
    return gameReleaseDate

def findPicURL(x):
    for i in gameDataElements[x]["keyImages"]:
        if i["type"] == "DieselStoreFrontWide":
            return i["url"]
    return gameDataElements[x]["keyImages"][0]   

def getFreeGames():
    y = []
    for x in range(len(gameDataElements)):
        y.append([gameDataElements[x]["id"],gameDataElements[x]["title"]])
    return y

#Game Details = {name, company, date, active_status, image_url, game_url, og_price}

def getGameDetails(name):
    for x in range(len(gameDataElements)):
        if gameDataElements[x]["title"] == name:
            if gameDataElements[x]["productSlug"] == None:
                if gameDataElements[x]["urlSlug"] == None:
                    urlgen = "not-found"
                else:
                    urlgen = gameDataElements[x]["urlSlug"]
            else:
                urlgen = gameDataElements[x]["productSlug"]
            
            print(f"Fetched game details for {name}")
            return [gameDataElements[x]["title"], gameDataElements[x]["seller"]["name"], getGameReleaseDate(x), gameDataElements[x]["status"], findPicURL(x), "https://www.epicgames.com/store/en-US/p/" + urlgen, gameDataElements[x]["price"]["totalPrice"]["fmtPrice"]["originalPrice"], gameDataElements[x]["id"]]

def isOfferActive(name):
    for x in range(len(gameDataElements)):
        if gameDataElements[x]["title"] == "Mystery Game":
            return False
        elif gameDataElements[x]["title"] == name:
            if pytz.utc.localize(datetime.datetime.strptime(getGameReleaseDate(x), "%Y-%m-%d")) <= datetime.datetime.now(tz = pytz.utc):
                print("Detected that a  game has active offers")
                return True
            else:
                return False

# gameDataElements[x]["promotions"]["promotionalOffers"][0]["promotionalOffers"][0]["startDate"][:10]