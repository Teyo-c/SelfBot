import os
import asyncio
import discord
from datetime import datetime
from keep_alive import keep_alive
import pytz

EU = pytz.timezone('Europe/Paris')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Règle son horloge"))

async def change_status():
    await client.wait_until_ready()
    while not client.is_closed():
        t = datetime.now(EU)
        horaire = " ⏲"
        horaire += t.strftime("%H:%M:%S")
        horaire += " ⏲"
        await client.change_presence(activity=discord.Game(name=horaire))
        await asyncio.sleep(5)

keep_alive()

client.loop.create_task(change_status())

client.run(os.getenv('TOKEN'),bot=False)