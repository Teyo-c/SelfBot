import discord
import os
import time
import asyncio
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Règle son horloge"))


async def change_status():
    await client.wait_until_ready()
    while not client.is_closed():
        t = time.gmtime()
        Heure = time.strftime("%H", t)
        Min = time.strftime("%M", t)
        horaire = "⏲"
        horaire+=str(int(Heure)+1)
        horaire+=":"
        horaire+=Min
        horaire += ":"
        horaire += time.strftime("%S", t)
        horaire += "⏲"
        await client.change_presence(activity=discord.Game(name=horaire))
        await asyncio.sleep(5)

keep_alive()

client.loop.create_task(change_status())

client.run(os.getenv('TOKEN'),bot=False)