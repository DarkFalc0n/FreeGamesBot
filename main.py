import os
import discord
from dotenv import load_dotenv
from setupmanager import setup

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '@setup':
        setup(message.guild.id, message.guild.id)
        print(f'Setup for server #{message.guild.id} complete.')
        await message.channel.send("This channel will now receive free game updates.")
       

    

client.run(token)