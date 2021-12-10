import discord
import os
import requests
import json
import status
import random

from random import sample
from discord.ext import commands
from discord.utils import get
from keep_alive import keep_alive
from lists import dog
from lists import cat
from lists import xmas
from lists import shiba
from lists import cope
from lists import cookie
from lists import trump

client = discord.Client()

bot = commands.Bot(command_prefix="$")

my_secret = os.environ['TOKEN']

@client.event
async def on_ready():
     await client.change_presence(activity=discord.Game('🎅Merry🎄Christmas☃️'))
     print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
       return
    
    if message.content.startswith('$start'):
        await message.channel.send("https://i.imgur.com/kYLxEbW.png")
    if message.content.startswith('$help'):
        await message.channel.send("https://i.imgur.com/kYLxEbW.png")
    if message.content.startswith('$hello'):
        await message.channel.send("HI!")
    if message.content.startswith('$invite'):
         embedVar = discord.Embed(title="INVITE", description="https://bit.ly/LAMBOT-invite", color=0x00ff00)
         embedVar.set_thumbnail(url="https://i.imgur.com/RemlzI6.jpg")
         await message.channel.send(embed=embedVar)
    if message.content.startswith('$commands'):
        embedVar = discord.Embed(title="GENERAL", description="$hello - say hi | $ban - ban any1 (FAKE) | $admin - gives u admin (FAKE) | $invite - invite LAM(BOT) to ur server | $help - get help | $commands - get commands | $code - get the code for this bot | $pfp - get the bots pfp |", color=0x00ff00)
        embedVar.add_field(name="FUN", value="$cat - get a cat pic | $shiba - get shiba $xmas - gifs of snow | $dog - gifs of dogs | $cope - cope | $cookie - get a pic of a cookie | $trump - random trump gif", inline=False)
        embedVar.add_field(name="INVITE", value="https://bit.ly/LAMBOT-invite", inline=False)
        embedVar.set_thumbnail(url="https://i.imgur.com/RemlzI6.jpg")
        await message.channel.send(embed=embedVar)
    if message.content.startswith('$dog'):
        await message.channel.send(random.sample(dog, 1))
    if message.content.startswith('$shiba'):
        await message.channel.send(random.sample(shiba, 1))
    if message.content.startswith('$cat'):
        await message.channel.send(random.sample(cat, 1))
    if message.content.startswith('$xmas'):
        await message.channel.send(random.sample(xmas, 1))
    if message.content.startswith('$ban'):
        await message.channel.send('https://c.tenor.com/BtC0jVjzYToAAAAM/loading-chain.gif')
    if message.content.startswith('$admin'):
        await message.channel.send('https://c.tenor.com/BtC0jVjzYToAAAAM/loading-chain.gif')
    if message.content.startswith('fuck u lambo'):
        await message.channel.send('https://c.tenor.com/Cbds_gTXfCcAAAAM/kick.gif')
    if message.content.startswith('fuck you lambo'):
        await message.channel.send('https://c.tenor.com/Cbds_gTXfCcAAAAM/kick.gif')
    if message.content.startswith('Fuck u lambo'):
        await message.channel.send('https://c.tenor.com/Cbds_gTXfCcAAAAM/kick.gif')
    if message.content.startswith('Fuck you lambo'):
        await message.channel.send('https://c.tenor.com/Cbds_gTXfCcAAAAM/kick.gif')
    if message.content.startswith('$cope'):
        await message.channel.send(random.sample(cope, 1))
    if message.content.startswith('$code'):
        await message.channel.send("https://www.mediafire.com/file/r8mkl83aoex3bh2/LAMBOT_%25286%2529.zip/file")
    if message.content.startswith('$sourcecode'):
        await message.channel.send("https://www.mediafire.com/file/r8mkl83aoex3bh2/LAMBOT_%25286%2529.zip/file")
    if message.content.startswith('$source'):
        await message.channel.send("https://www.mediafire.com/file/r8mkl83aoex3bh2/LAMBOT_%25286%2529.zip/file")
    if message.content.startswith('apollo is good'):
        await message.channel.send("https://c.tenor.com/_4K_0sndwtEAAAAj/green-white.gif")
    if message.content.startswith('apollo is great'):
        await message.channel.send("https://c.tenor.com/_4K_0sndwtEAAAAj/green-white.gif")
    if message.content.startswith('apollo is the best'):
        await message.channel.send("https://c.tenor.com/_4K_0sndwtEAAAAj/green-white.gif")
    if message.content.startswith('apollo is the goat'):
        await message.channel.send
    if message.content.startswith('APOLLO is good'):
        await message.channel.send("https://c.tenor.com/_4K_0sndwtEAAAAj/green-white.gif")
    if message.content.startswith('APOLLO is great'):
        await message.channel.send("https://c.tenor.com/_4K_0sndwtEAAAAj/green-white.gif")
    if message.content.startswith('APOLLO is the best'):
        await message.channel.send("https://c.tenor.com/_4K_0sndwtEAAAAj/green-white.gif")
    if message.content.startswith('APOLLO is the goat'):
       await message.channel.send("https://c.tenor.com/_4K_0sndwtEAAAAj/green-white.gif")
    if message.content.startswith('$pfp'):
       await message.channel.send("https://i.imgur.com/RemlzI6.jpg")
    if message.content.startswith('$cookie'):
        await message.channel.send(random.sample(cookie, 1))
    if message.content.startswith('$fn'):
        await message.channel.send("https://fortnitetracker.gg/profile/v2/GAMER_BREAD_11")
    if message.content.startswith('$FN'):
        await message.channel.send("https://fortnitetracker.gg/profile/v2/GAMER_BREAD_11")
    if message.content.startswith('$rap'):
        await message.channel.send("https://www.youtube.com/watch?v=NHiUQb5xg7A")
    if message.content.startswith('$RAP'):
        await message.channel.send("https://www.youtube.com/watch?v=NHiUQb5xg7A")
    if message.content.startswith('$TRUMP'):
        await message.channel.send(random.sample(trump, 1))
    if message.content.startswith('$trump'):
        await message.channel.send(random.sample(trump, 1))
    if message.content.startswith('$driver'):
        await message.channel.send("https://www.nvidia.com/Download/index.aspx?lang=en-us")





keep_alive()
client.run(os.getenv('TOKEN'))
