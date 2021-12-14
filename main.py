import os
import discord, asyncio
from os import system
import subprocess
from discord.ext import commands

print("""tu mama es puta jaja""")

client = discord.Client()

def murder(cmd):
    subprocess.call(cmd, shell=False)

@client.event
async def on_ready():

    width = shutil.get_terminal_size().columns
 
    def ui():
        print("auth user: {0} ".format(client.user))
        print()
    ui() 
 
@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel

        if commands[0] == '.':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=9999):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass

client.run(os.environ['token'], bot=False)
