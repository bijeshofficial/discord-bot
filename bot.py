import discord
from decouple import config
client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('hello, I am a bot')

try:
    print("Bot is Alive")
except:
    print("Bot is malfuinctioning")

client.run(config('DISCORD_TOKEN'))
