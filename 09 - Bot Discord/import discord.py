from importlib.resources import contents
from itertools import count
import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os

#Variaveis ocultas
load_dotenv()
token = os.getenv('token')
insta = os.getenv('insta')




async def on_ready():
    print('We have logged in as {0.user}'.format(client))
#Mensagens por comandos:
class MyClient(discord.Client):
    async def on_message(self, message):

        if message.content == '!teste':
            await message.channel.send()
        #brava
        if message.content == '!brava':
            ig = random.choice(insta)
            brava= 'https://www.instagram.com/' + ig
            await message.channel.send(brava)
       
client = MyClient()
client.run(token)

        
