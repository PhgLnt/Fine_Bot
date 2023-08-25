# import discord
import os

import nextcord
# from gtts import gTTS
from dotenv import load_dotenv
import responses
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True  # This enables message content in the events
bot = commands.Bot(command_prefix='f', intents=intents)

client = nextcord.Client(intents=intents)

load_dotenv()
TOKEN = os.environ.get('TOKEN')

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        if response is not None:
            if is_private:
                await message.author.send(response)
            else:
                await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'
              .format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        # username = str(message.author)
        user_message = str(message.content)
        # channel = str(message.channel)

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
