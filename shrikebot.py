import discord
import os
from enum import Enum

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True

client = discord.Client()


class Command(Enum):
    COMMAND = '!commands'
    HELLO = '!hello'
    MEETING = '!meeting'

    def allcommands(self):
        commands = ''
        for vals in Command:
            commands = commands + '{} '.format(vals.value)
        return  commands

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(Command.HELLO):
        user = str(message.author)
        users = user.split('#')
        print(users[0])
        await message.channel.send('Hello {0}!'.format(users[0]))
    if message.content.startswith(Command.COMMAND):
        msg = 'Bot commands are: ' + Command.allcommands()
        await message.channel.send(msg)


@client.event
async def on_member_join(member):
    print('got a thing')
    print(member.name)
    channel = client.get_channel(906596208112451648)  ## this is the general chat
    # channel = client.get_channel(906651114127122484)  ## this is the private bot testing chat
    await channel.send('Welcome to this channel, {0}!'.format(member.name))


@client.event
async def on_member_remove(member):
    print('lost a member')


client.run(os.environ['TOKEN'])
