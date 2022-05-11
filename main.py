import os
import time
import urllib.request
from getpass import getpass
from colorama import Fore, Back, Style
import getpass 


passwd = urllib.request.urlopen("pastebin url here")
passutf = passwd.read().decode("utf8")
passutf = passutf.split("\r\n")


banner = ("""


| Sample-Login | 1.0
|══════════════════════════════════════════════
| By DEUS-WEB#9999
| Discord : discord.gg/deusweb
|══════════════════════════════════════════════
| Enter your key lisence.
""")

def menu():
    print(Fore.GREEN + "Succesfully login ! thanks you")

def login():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.BLUE + banner)
    pwd = getpass.getpass(prompt = Fore.BLUE + "Key: ")
    if pwd in passutf: 
       os.system('cls' if os.name == 'nt' else 'clear')
       print(Fore.GREEN + "Succes key!")
       menu()
    else: 
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + "Wrong key!")
login()