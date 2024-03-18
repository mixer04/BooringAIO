from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions, Chrome
import os
import zipfile
from selenium import webdriver
import threading
from threading import Thread, Barrier
import pyautogui
from colorama import Fore, Back, Style
import colorama
import pypresence
from pypresence import Presence
import pyfiglet
import time
from datetime import datetime
import random
from seleniumwire import webdriver

now = datetime.now()
current_time = now.strftime("%H:%M:%S.%f").rstrip('0')

colorama.init()




PROXY_HOST = ''  # rotating proxy or host
PROXY_PORT = '' # port
PROXY_USER = '' # username
PROXY_PASS = '' # password


manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

def get_chromedriver(use_proxy=False, user_agent=None):
    path = os.path.dirname(os.path.abspath(__file__))
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        chrome_options.add_extension(pluginfile)
    if user_agent:
        chrome_options.add_argument('--user-agent=%s' % user_agent)
    driver = webdriver.Chrome(
        os.path.join(path, 'chromedriver'),
        chrome_options=chrome_options)
    return driver

now = datetime.now()
current_time = now.strftime("%H:%M:%S.%f").rstrip('0')
print("[" + current_time + "]" + Fore.YELLOW + " Set URL you want to open:" + Style.RESET_ALL)

URL = input()


now = datetime.now()
current_time = now.strftime("%H:%M:%S.%f").rstrip('0')
print("[" + current_time + "]" + Fore.YELLOW + " Set how many threads you want to open:" + Style.RESET_ALL)

NUM_THREADS = int(input())
thread_list = list()

# Wait for all thre<ads to complete
for thread in thread_list:
    thread.join()

def main():
    for i in range(0, NUM_THREADS):
        t = threading.Thread(name=' Instance', target=URL)
        driver = get_chromedriver(use_proxy=True)
        driver.set_window_size(1400, 800)
        driver.execute_script("document.body.style.zoom='zoom10%'")
        driver.get(URL)
        time.sleep(1)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S.%f").rstrip('0')
        print("[" + current_time + "]" + Fore.GREEN + t.name + " started" + Style.RESET_ALL)
    
    sleep(99999)

if __name__ == '__main__':
    main()
