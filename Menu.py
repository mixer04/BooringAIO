from consolemenu import *
from consolemenu.items import *
import os
import asyncio
import pypresence
from pypresence import Presence
import pyfiglet
import time
from pyfiglet import Figlet
from os import system
import ctypes
from colorama import Fore, Back, Style
import colorama
import dotenv
import json
from random_user_agent.params import SoftwareName, HardwareType
from random_user_agent.user_agent import UserAgent
import requests as rq
import logging
import re
import uuid
import requests
from datetime import datetime
import webdriver_auto_update
from webdriver_auto_update import check_driver
import sys
import subprocess
import threading
import zipfile
import pyautogui

subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r' 
'requirements.txt'])

now = datetime.now()
current_time = now.strftime("%H:%M:%S.%f").rstrip('0')

colorama.init()

CONFIG = dotenv.dotenv_values()


ctypes.windll.kernel32.SetConsoleTitleW("BooringAIO")

API_KEY = ''

def discord():
    client_id = '' #Put your client ID here
    RPC = Presence(client_id) 
    RPC.connect() 
    print(RPC.update(state="0.0.1", details="Cooking...", large_image="ikona1000", small_image="ikona1000", start=time.time()))  # Set the 


discord()
os.system('cls||clear')
print('\n')
custom_fig = Figlet(font='slant')
print(custom_fig.renderText('BooringAIO'))
print('\n')

print("[" + current_time + "]" + Fore.GREEN + " Checked All Requirements" + Style.RESET_ALL)
time.sleep(2)
now = datetime.now()
current_time = now.strftime("%H:%M:%S.%f").rstrip('0')
print("[" + current_time + "]" + Fore.YELLOW + " Checking Chrome Driver..." + Style.RESET_ALL)
time.sleep(2)
check_driver('chromedriver')
time.sleep(1)
now = datetime.now()
current_time = now.strftime("%H:%M:%S.%f").rstrip('0')
print("[" + current_time + "]" + Fore.GREEN + " Chrome Driver Checked" + Style.RESET_ALL)
time.sleep(2)

now = datetime.now()
current_time = now.strftime("%H:%M:%S.%f").rstrip('0')
print("[" + current_time + "]" + Fore.YELLOW + " Checking License..." + Style.RESET_ALL)
time.sleep(2)


def get_license(license):
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }

    req = requests.get(f'https://api.hyper.co/v4/licenses/{license}', headers=headers)
    if req.status_code == 200:
        return req.json()

    return None

with open('data/config.json') as json_data_file:
    config = json.load(json_data_file)
    using_recover = config['recovery']
    ac_token = config['anticaptchatoken']
    headless = config['headless']
    password = config['password']
    locale = config['locale']
    dscwebhook = config['dscwebhook']
    pi = config['saapi']
    license = config['license']


license_data = get_license(license)
if license_data:
    if license_data.get('metadata') != {}:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S.%f").rstrip('0')
        print("[" + current_time + "]" + Fore.RED + " License is already in use on another machine!" + Style.RESET_ALL)
        time.sleep(2)
        exit()
    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S.%f").rstrip('0')
        print("[" + current_time + "]" + Fore.GREEN + " License is good to go!" + Style.RESET_ALL)
        time.sleep(2)
else:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f").rstrip('0')
    print("[" + current_time + "]" + Fore.RED + " License not found!" + Style.RESET_ALL)
    time.sleep(2)
    exit()


def update_license(license, hardware_id):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    payload = {
        'metadata': {
            'hwid': hardware_id
        }
    }

    req = requests.patch(f'https://api.hyper.co/v4/licenses/{license}', headers=headers, json=payload)
    if req.status_code == 200:
        return True

    return None

def reset_license(license, hardware_id):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    payload = {
        'metadata': {
            'hwid': hardware_id
        }
    }

    req = requests.patch(f'https://api.hyper.co/v4/licenses/{license}', headers=headers, json=payload)
    if req.status_code == 200:
        return True
  
    return None


os.system('cls||clear')

print('\n')
custom_fig = Figlet(font='slant')
print(custom_fig.renderText('BooringAIO'))

print('\n')
print(Fore.YELLOW + "--------MENU--------")
print('\n')

def menu():
    print(Fore.YELLOW + "[1] Chrome Module")
    print("[2] Test Webhook")
    print("[0] Exit")
    print(Fore.RESET + "")
    

def option1():
    print(Fore.MAGENTA + "[" + "BooringAIO" + "]" + " Chrome module is starting..." + Style.RESET_ALL)
    os.system('python chrome.py')

def option2():
    print(Fore.MAGENTA + "[" + "BooringAIO" + "]" + " Opening settings..." + Style.RESET_ALL)

def test_webhook():
    """
    Sends a Discord webhook notification to the specified webhook URL
    """
    data = {
        "username": CONFIG['USERNAME'],
        "avatar_url": CONFIG['AVATAR_URL'],
        "embeds": [{
            "title": "Testing Webhook",
            "description": "Everything Works!!",
            "color": int(CONFIG['COLOUR']),
            "footer": {'text': 'BooringAIO'},
            "timestamp": str(datetime.utcnow())
        }]
    }
    result = rq.post(dscwebhook, data=json.dumps(data), headers={"Content-Type": "application/json"})
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f").rstrip('0')
    print("[" + current_time + "]" + Fore.CYAN + " Webhook sent!" + Style.RESET_ALL)




menu()
option = int(input("Enter your choice:" + " "))

while option != 0:
    if option == 1:
        option1()
    elif option == 2:
        test_webhook()  
    else:
        print("Invalid option.")

    option = int(input("Enter your choice:" + " "))

now = datetime.now()
current_time = now.strftime("%H:%M:%S.%f").rstrip('0')
print("[" + current_time + "]" + Fore.MAGENTA + " Thanks for using BooringAIO. See you soon!" + Style.RESET_ALL)
time.sleep(2)
exit()
