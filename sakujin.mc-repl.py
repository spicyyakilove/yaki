import discord
import os
import requests
import json
import random
from replit import db


client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('@ping'):
    await message.channel.send('Pong! ??? ms')

  if msg.startswith('@creator'):
    await message.channel.send('Spicyyakisoba, a mother of 16 children. The programmer of the bot Sakujin.')
  
  if msg.startswith('@info.leeknow'):
    await message.channel.send('Lee Know. or Lee Min Ho, was born on October 25, 1998, and is a member of the group Stray Kids. He is a scorpio and is 172 cm short. His blood type is O. He is associated with Des, and is her boyfriend.')
  
  if msg.startswith('$lk.minsoul'):
    await message.channel.send('Minsoul: Lee Know https://media.discordapp.net/attachments/791578185761816588/806011872989675542/ily.gif')
  
  if msg.startswith('@rerun ping'):
    await message.channel.send('# SAKUJIN V1 TEST COMMAND: PING // FAILED! **PING not found.**')

client.run(os.getenv('TOKEN'))