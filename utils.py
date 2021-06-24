from epicrequests import getFreeGames, getGameDetails, isOfferActive
import discord
import datetime

def newGameAvailable():
    p = False
    f = open("./update_data/Updated_EGS.txt", "r")
    x = (f.read().split("\n"))
    y = getFreeGames()
    for i in y:
        if x.count(i) == 0 and isOfferActive(i):
            p = True
    return p

def dateConvert(date):
    d = datetime.datetime.strptime("date", "%Y-%m-%d")
    return datetime.date.strftime(d, "%d %B %Y")

#Game Details = {name, company, date, active_status, image_url, game_url, og_price}
def newGameEmbed():

    y = getFreeGames()
    f = open("./update_data/Updated_EGS.txt", "r")
    x = (f.read().split("\n"))
    for i in y:
        if x.count(i) == 0:
            details = getGameDetails(i)
        break
    embed = discord.Embed(title = details[0], url = details[5], description = "Free on Epic Games from: " + dateConvert(details[3]), color = 0xff7b47)
    embed.add_field(name = "Original Price", value=details[6], inline=True)
    embed.add_field(name = "Offer Status", value=details[3], inline=True)
    embed.set_image(url = details[4])
    embed.set_footer(text = "Claim the free game")
    f = open("./update_data/Updated_EGS.txt", "a")
    f.write(i + "\n")
    print(f"Created an embed for game: {details[0]}")
    return embed

