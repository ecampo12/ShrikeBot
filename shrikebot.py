import discord
import os

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        user = str(message.author)
        users = user.split('#')
        print(users[0])
        await message.channel.send('Hello {0}!'.format(users[0]))


@client.event
async def on_member_join(member):
    print('got a thing')
    channel = client.get_channel(906596208112451648) ## this is the general chat
    # channel = client.get_channel(906651114127122484)  ## this is the private bot testing chat
    await channel.send('Welcome to this channel!')


@client.event
async def on_member_remove(member):
    print('lost a member')


client.run(os.environ['TOKEN'])
