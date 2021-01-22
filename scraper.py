from bs4 import BeautifulSoup # pip install bs4
import requests # pip install requests
import os # default
import json # default
import time # possibly default

link = 'https://duckduckgo.com/?q=donkey+face&atb=v236-1&iax=images&ia=images'

user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}

def clear():
    os.system('cls')

def main():
    clear()

    print('Welcome to the donkey image saver :D')
    print('Here are the possible commands:')
    print('settings -> lets you change the number of images to save, URL to save from and where to save')
    print('start -> starts saving images')

    mainInput = input()
    
    if mainInput == 'start':
        saveimgs()
    elif mainInput == 'settings':
        settings()
    else:
        print('Invalid Input.')
        time.sleep(3)
        main()

def settings():
    clear()
    
    print('What would you like to change?')
    print('1 - URL to save from\n2 - numbers of images to save')

    settingsInput = int(input())

    if settingsInput == 1:
        new_link()
        main()
    elif settingsInput == 2:
        img_num()
        main()
    else:
        print('Invalid Input.')
        time.sleep(3)
        settings()

def new_link():
    print("Paste a link to go off of (for now use duckduckgo):")
    link = input()
    main()

def img_num():
    img2save = int(input('How many images should I save? '))
    main()

def foldercheck():
    if not os.path.exists('donkey_imgs'):
        os.mkdir('donkey_imgs')

def saveimgs():
    clear()
    print('Current URL: ' + link)
    foldercheck()

main()