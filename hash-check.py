#!/usr/bin/python3.6

from time import time, sleep

import bs4
import requests
import tqdm
from tqdm import tqdm
import pyfiglet
import time
import timeit
import os
import readline
from random import choice


desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; rv:11.0) like Gecko',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MATBJS; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)',
                  'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; PRU_IE; rv:11.0) like Gecko',
                  'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
                  'Mozilla/5.0 (Linux; U; Android 4.0.3; en-ca; KFOT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36']


def space():
    print()
    print()


def banner():
    sulat = pyfiglet.figlet_format('   Hash', font="roman")
    sulat2 = pyfiglet.figlet_format(' Check ', font="roman")
    print(u'\u001b[36;1m')
    print(sulat + sulat2)
    print(u'\u001b[0m')
    print(u'This application can \u001b[31mDetect\u001b[0m and \u001b[31mDecrypt\u001b[0m the following:')
    print(u'[\u001b[31mx\u001b[0m] md5')
    print(u'[\u001b[31mx\u001b[0m] sha1')
    print(u'[\u001b[31mx\u001b[0m] sha256')
    print(u'[\u001b[31mx\u001b[0m] sha356')
    print(u'[\u001b[31mx\u001b[0m] sha512')
    print()
    print(u'Type \u001b[32mHelp\u001b[0m for options.\n')
    print()


# Para Reference
def pbar():
    with tqdm(total=100, desc="Finding Match") as pbar:
        counter = 0
        while counter < 100:
            sleep(1)
            counter += 10
            pbar.update(10)


def bar():
    for i in tqdm(range(0, 100), desc="Finding Match"):  # unit=' Nanosecond'
        sleep(10)
        # val = i


def oras():
    t1 = time.time()
    for x in range(1, 100):
        # t2 = time.time()
        y = str(time.process_time() - t1)

    print('Execution Time:' + y + " n/s")

def help():
    print()
    print('------ Help Function -------')
    print()
    print(u' \u001b[36mClear\u001b[0m \tTo clear output. ')
    print(u' \u001b[36mExit\u001b[0m  \tTo exit the program. ')
    print(u' \u001b[36mHelp\u001b[0m  \tTo display this info. ')
    print(u' \u001b[36mIP\u001b[0m  \tTo display IP info. ')
    print(u' \u001b[36mUA\u001b[0m  \tTo display User Agent info. ')
    print()

def out():
    print()
    print('------ Thank You  -------')
    print()

def proc():
    y = 'https://sslproxies.org/'
    r1 = requests.get(y)
    sopas = bs4.BeautifulSoup(r1.text, 'html.parser')
    s1 = sopas.find_all('td')[0] # first index
    s2 = sopas.find_all('td')[1]
    s3 = str(s1.text + ':' + s2.text)
    print('We will be using this IP address: ' + s3)


def random_headers():
    return {'User-Agent': choice(desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}








##-------------------- Program Execute's here -------------





banner()  # Banner
random_headers()
proxies = proc()


while True:
    try:
        random_headers()
        print()
        miswa = input('Enter Hash: ')
        print()
        if miswa == "Exit" or miswa == "exit":
            print("Thank You.")
            break

        elif miswa == "Help" or miswa == "help":
            help()
            continue

        elif miswa == "Clear" or miswa == "clear":
            os.system('clear')
            continue

        elif miswa == "IP" or miswa == "ip":
            proc()
            continue

        elif miswa == "UA" or miswa == "ua":
            r1 = random_headers()
            r2 = list(r1.values())
            r3 = str(r2)
            r4 = str(r3.replace(",", ''))
            r5 = str(r4.replace("[", ''))
            r6 = str(r5.replace("]", ''))
            r7 = str(r6.replace("'", ''))
            r8 = str(r7.replace("(", ''))
            r9 = str(r8.replace(")", ''))
            print(r9.replace(' ', '\n'))
            continue

        else:
            start = timeit.default_timer()  # TIMEIT module
            patola = 'https://hashtoolkit.com/reverse-hash/?hash='
            kamote = requests.get(patola + miswa, headers=random_headers(), proxies = proxies)


            soup = bs4.BeautifulSoup(kamote.text, "html.parser")


            x2 = miswa
            x = soup.find("td", {"class": "res-text"})
            x1 = x

            print(u"Algorithm Type:\u001b[32m  " + soup.td.text)
            print(u"\u001b[0mDecrypted Value:\u001b[32m " + (x1.text).strip('\t\r\n'))
            print(u'\u001b[0m')

            stop = timeit.default_timer()
            y = str(stop - start)  # TIMEIT module

            print(str('Execution Time: ' + (y[0:8]) + " /s"))  # Time display for execution
            print()

















    except:
        print(" Unable to find possible match !!.\n Network connectivity can also be a reason. \n Please try again.")
        #print(e)
        print()
