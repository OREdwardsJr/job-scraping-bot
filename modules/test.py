import os
import nest_asyncio
nest_asyncio.apply()


import discord
from dotenv import load_dotenv
load_dotenv('---.env')

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#A client is an object that represents a connection to discord
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
            
    print(
    f'{client.user} is connected to the following guild:\n'
    f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    
client.run(TOKEN)