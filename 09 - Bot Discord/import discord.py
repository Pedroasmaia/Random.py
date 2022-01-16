from itertools import count
import discord
import random
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('token')

class MyClient(discord.Client):
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!teste':
            await message.channel.send('teste')
   

client = MyClient()
client.run(token)

        
