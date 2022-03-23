import os
import discord
import json
import random
from keep_alive import keep_alive


client = discord.Client()

perc_words = ["kanye", "hello","west","and", "donda","kanye"]

perc_sayings = [
  "We all self-conscious. I'm just the first to admit it.",
  "I am God's vessel. But my greatest pain in life is that I will never be able to see myself perform live.",
  "In jesus name, no more cap",
  "I no longer have a manager, I can not be managed",
  "WHERE THE PROBLEM AT, IM SPINNIG ON THESE PERCS LIKE IM A LAUNDROMAT / bot!",
  "find god"
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

