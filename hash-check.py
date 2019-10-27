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


def space():
    print()
    print()


def banner():
    sulat = pyfiglet.figlet_format('   Hash', font="roman")
    sulat2 = pyfiglet.figlet_format(' Check ', font="roman")
    print(u'\u001b[36;1m')
    print(sulat + sulat2)
    print(u'\u001b[0m')
    print(u'This application can \u001b[31mDetect\u001b[0m and \u001b[31mDecrypt\u001b[0m the following:\n')
    print(u'[\u001b[31mx\u001b[0m] md5')
    print(u'[\u001b[31mx\u001b[0m] sha1')
    print(u'[\u001b[31mx\u001b[0m] sha256')
    print(u'[\u001b[31mx\u001b[0m] sha356')
    print(u'[\u001b[31mx\u001b[0m] sha512')
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
    print(u' Clear \tTo clear output. ')
    print(u' Exit  \tTo exit the program. ')
    print(u' Help  \tTo display this info. ')
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
    print(' We will be using this IP address: ' + s3)









##-------------------- Program Execute's here -------------



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
banner()  # Banner
proxies = proc()

while True:
    try:

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

        else:
            start = timeit.default_timer()  # TIMEIT module
            patola = 'https://hashtoolkit.com/reverse-hash/?hash='
            kamote = requests.get(patola + miswa, headers=headers, proxies = proxies)


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
