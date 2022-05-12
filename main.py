import os
import time
import requests
import urllib.request
from getpass import getpass
from colorama import Fore, Back, Style
import getpass 

#modify the link by putting the connection keys
passwd = urllib.request.urlopen("https://pastebin.com/raw/p5XBSN31")
passutf = passwd.read().decode("utf8")
passutf = passutf.split("\r\n")

#edit variable VERSION for uptdate
VERSION = "1.1"
#edit link version (raw)
version = requests.get("https://pastebin.com/raw/ScLewjnu").content.decode('utf-8')

banner = (f"""
| Sample-Login | {VERSION}
|══════════════════════════════════════════════
| By DEUS-WEB#9999
| Discord : discord.gg/deusweb
|══════════════════════════════════════════════
| Welcome to Sample-Login.
""")


def menu():
    print(Fore.YELLOW + "> " + Fore.GREEN + "Succesfully login ! thanks you")

def login():
  if version != VERSION:
    
    print(Fore.YELLOW + "> " + Fore.RED + "Update available")
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.BLUE + banner)
    pwd = getpass.getpass(prompt = Fore.YELLOW + "> " + Fore.BLUE + "Key: ")
    if pwd in passutf: 
       os.system('cls' if os.name == 'nt' else 'clear')
       menu()
    else: 
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.YELLOW + "> " + Fore.RED + "Wrong key!")
login()
