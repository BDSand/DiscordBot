import os
import discord
import json
import random
from keep_alive import keep_alive


client = discord.Client()

perc_words = ["perc", "perc30","boof","faded", "yeat","molly"]

perc_sayings = [
  "I need a perc",
  "2pm, time for a perc!",
  "who needs percs!",
  "stummy hurt",
  "WHERE THE PROBLEM AT, IM SPINNIG ON THESE PERCS LIKE IM A LAUNDROMAT / bot!"
]
#When bot is working
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#when recieves message
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content

  if message.content.startswith('$hello'):
   await message.channel.send('Stop Chatting, go find God, comeback when you found God') 
  if any(word in msg for word in perc_words):
    await message.channel.send(random.choice(perc_sayings)) 

#run the bot
keep_alive()
client.run(os.environ['TOKEN'])

