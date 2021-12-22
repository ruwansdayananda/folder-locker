from genericpath import exists
import os.path
import os
from os import path
import bcrypt
import json
from termcolor import colored, cprint
import termcolor
import time
import stdiomask

salt = bcrypt.gensalt()

def fail():
    print(colored("Invalid Password","red"))
    time.sleep(2)

def unlock():
    user_input = stdiomask.getpass(mask="•",prompt="Enter password to Unlock Your Secure Folder: ")
    with open(os.path.join('Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}','config.json'), 'r',encoding='utf-8') as openfile: 
        config_data = json.load(openfile)
    if(not bcrypt.checkpw(user_input.encode('utf-8'), config_data['password'].encode('utf-8'))):
        fail()
    else:
        os.system('attrib -r -h -s /s /d "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
        os.system('attrib -r -h -s /s /d "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}\*.*"')
        os.rename("Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}","Private")
        print(colored("Folder has been unlocked successfully !","green"))
        time.sleep(2)

def makePrivate():
    os.mkdir("Private")
    print(colored("Private folder has been created !","green"))
def lock():
    os.rename("Private","Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}")
    os.system('attrib +r +h +s /s /d "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}\*.*"')
    os.system('attrib +r +h +s /s /d "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
    print(colored("Folder has been locked !","yellow"))
    time.sleep(2)
def confirm():
    ensure = input("Are you sure to lock this folder? (Y/N): ")
    if(ensure.lower()=='y'):
        lock()

def initializeConfig():
    master_password = input("Enter a master password: ")
    data = {'password':str(bcrypt.hashpw(master_password.encode('utf-8'),salt))[2:-1]}
    with open(os.path.join('Private','config.json'), 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file)

if(path.exists("Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}")):
    unlock()
elif(not path.exists("Private")):
    makePrivate()
    initializeConfig()
else:
    confirm()



