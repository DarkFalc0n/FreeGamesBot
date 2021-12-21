import os
from DBmanager import setup

from utils import newGameAvailable, newGameEmbed
import discord
from dotenv import load_dotenv
import pymongo
import asyncio
from epicrequests import requestData


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
connect = os.getenv('MongoDB_URL')

dbclient = pymongo.MongoClient(connect)
dataB = dbclient["FreeGamesBot"]
dataCol = dataB["Servers"]

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '*setup':
        setup(message.guild.id, message.guild.id)
        print(f'Setup for server #{message.guild.id} complete.')
        await message.channel.send("This channel will now receive free game updates.")


@client.event
async def on_Game_Release():
    while (True):
        if newGameAvailable() == True:
            requestData()
            channelList = dataCol.find({}, {'ChannelID':1, '_id':0})
            await client.wait_until_ready()
            for i in channelList:
                Cid = int(i["ChannelID"])
                channelToSend = client.get_channel(Cid)  
                await channelToSend.send("@everyone", embed = newGameEmbed())
            print ("Sent a new update to all channels")
        await asyncio.sleep(120)

client.loop.create_task(on_Game_Release())

   
    
client.run(token)