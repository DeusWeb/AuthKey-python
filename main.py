#import
import os
import random
import getpass 
import discord_webhook
import socket
import time
import urllib.request
import requests

#from
from colorama import Fore, Back, Style
from getpass import getpass
from discord_webhook import DiscordWebhook, DiscordEmbed

#variable
passwd = urllib.request.urlopen("pastebin password url")
passutf = passwd.read().decode("utf8")
passutf = passutf.split("\r\n")
VERSION = "1.1"

version = requests.get("pastebin version url").content.decode('utf-8')

ip = 'https://api.ipify.org/' 
output = requests.get(ip).text

#title for spotify logs
titlelogs = "Spotify Bot Logs"

banner = (f"""
| Sample-Login | v{version}
|══════════════════════════════════════════════
| By DEUS-WEB#9999
| Discord : discord.gg/deusweb
|══════════════════════════════════════════════
| Welcome to Sample-Login v1.2.
""")

def menu():
  os.system('cls' if os.name == 'nt' else 'clear')

def login():
  os.system('cls' if os.name == 'nt' else 'clear')
  if version != VERSION:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.BLUE + "[" + Fore.YELLOW + "!" + Fore.BLUE + "] " + Fore.GREEN + version)
    time.sleep(2.5)
    exit()
  else:
    print(Fore.BLUE + banner)
    pwd = input(Fore.BLUE + "[" + Fore.RED + "!" + Fore.BLUE + "] " + Fore.GREEN + "Key: ")
    if pwd in passutf: 
       os.system('cls' if os.name == 'nt' else 'clear')
       print(Fore.GREEN + "[" + Fore.YELLOW + "!" + Fore.GREEN + "] " + Fore.WHITE + "Succes key!")
       webhook = DiscordWebhook(url='Webhook logs url') 
       embed = DiscordEmbed(title='AuthKey login detected !', description="This key has been detected " + pwd + "\n With this ip " + output, color=0x1f8b4c)
       embed.set_author(name=titlelogs, url='https://github.com/deusweb', icon_url='https://cdn.discordapp.com/attachments/973770127214518292/974117000811003904/avatar-618278729-0.jpg')
       embed.set_footer(text='Credits: DEUS-WEB#9999')
       embed.set_timestamp()
       webhook.add_embed(embed)
       response = webhook.execute()
       time.sleep(2) 
       menu()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + "[" + Fore.YELLOW + "!" + Fore.RED + "] " + "Wrong key!") 
        time.sleep(3)
        login()

def loading():
    print(Fore.RED + "Wait....")
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    webhook = DiscordWebhook(url='Webhook logs url') 
    embed = DiscordEmbed(title='Suspicious connection detect !', description="This ip has been detected " + output, color=0x992d22)
    embed.set_author(name=titlelogs, url='https://github.com/deusweb', icon_url='https://cdn.discordapp.com/attachments/973770127214518292/974117000811003904/avatar-618278729-0.jpg')
    embed.set_footer(text='Credits: DEUS-WEB#9999')
    embed.set_timestamp()
    webhook.add_embed(embed)
    response = webhook.execute()
    login()


loading()
