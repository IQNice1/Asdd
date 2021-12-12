import os
import discord, asyncio
from os import system
import shutil
import subprocess
import socket, sys, discord, base64, threading, requests
from sys import argv
import psutil
import logging
from requests import get
from time import sleep
from discord.ext import commands
from colorama import init, Fore
from bs4 import BeautifulSoup
from os import system
from webserver import keep_alive
#import ctypes ctypes.windll.kernel32.SetConsoleTitleA("M")

init()
system("@echo off")
system("cls")
system("mode con: cols=105 lines=30")
system('title ' + 'urmom')

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

        if commands[0] == '#':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=9999):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass
keep_alive()
client.run(os.environ['token'], bot=False)
