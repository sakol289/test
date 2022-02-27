# -*- coding: utf-8 -*-

#เริ่มต้น import

import platform
import os
import time
from re import search
import asyncio
from time import gmtime, strftime
import threading
from time import sleep
from tqdm import tqdm
try:#เช็ค โมดูล
    from requests_futures.sessions import FuturesSession
    import platform
    import os
    import sys
    from re import search
    from wsgiref.validate import InputWrapper
    from requests import Session
    from threading import Thread
    from colorama import Fore, init
    from requests import get
    from requests_futures.sessions import FuturesSession
    import asyncio
    import time
    from tqdm import tqdm
    from datetime import datetime    
    print("hee")

except:#ถ้าไม่มีให้ติดตั้ง
    print("requests install...")
    os.system("pip3 install requests")
    print("platform install...")
    os.system("pip3 install platform")
    print("colorama install...")
    os.system("pip3 install colorama")
    print("FuturesSession install...")
    os.system("pip3 install requests-futures")
    print("asyncio install...")
    os.system("pip3 install asyncio")
    print("thread install...")
    os.system("pip3 install thread")
    print("tpdm install...")
    os.system(" pip3 install tqdm")
    exit()


#จบimport

def tpm():    
    try:
        for i in tqdm(range(10),ncols=60):
            sleep(0.05)
    except:
        pass
def run():
    os.system("apt-get update")
    os.system("apt-get upgrade")
    os.system("wget https://raw.githubusercontent.com/sakol289/bashterumxv1/main/bash.bashrc")
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("rm $HOME/../usr/etc/motd mv bash.bashrc $HOME/../usr/etc")
    os.system("mv banner.txt $HOME")
    
def start():
    run()
    tpm()
    
