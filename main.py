import os
from DBmanager import setup

from utils import newGameAvailable
import discord
from dotenv import load_dotenv
import pymongo
import asyncio

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
    if newGameAvailable() == True:
        channelList = dataCol.find({}, {ChannelID:1, _id:0, strict:0})
        for i in channelList:
            channel = client.get_channel(i)
            await channel.send(newGameEmbed())
        print ("Sent a new update to all channels")
    await asyncio.sleep(300)
    
client.loop.create_task(on_Game_Release())   
    
client.run(token)