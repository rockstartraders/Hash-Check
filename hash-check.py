#!/usr/bin/python3.6

from time import time, sleep

import bs4
import requests
import tqdm
from tqdm import tqdm
import pyfiglet
import time
import timeit
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





##-------------------- Program Execute's here -------------




banner()  # Banner

while True:
    try:


        miswa = input('Enter Hash: ')

        print()

        start = timeit.default_timer()  # TIMEIT module
        patola = 'https://hashtoolkit.com/reverse-hash/?hash='
        kamote = requests.get(patola + miswa)


        soup = bs4.BeautifulSoup(kamote.text, "html.parser")


        x2 = miswa
        x = soup.find("td", {"class": "res-text"}).text
        x1 = str(x.text)

        print(u"Algorithm Type:\u001b[32m  " + soup.td.text)
        print(u"\u001b[0mDecrypted Value:\u001b[32m " + str(x1.text).strip('\t\r\n'))
        print(u'\u001b[0m')

        stop = timeit.default_timer()
        y = str(stop - start)  # TIMEIT module

        print(('Execution Time: ' + str(y[0:8]) + " /s"))  # Time display for execution
        print()

















    except Exception as e:
        # print(" Unable to find possible match !! ")
        print(e)
        print()
