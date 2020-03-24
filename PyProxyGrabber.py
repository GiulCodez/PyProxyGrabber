#libarys used
import sys
import requests
import time 
import os 
import colored #need to download youself
print ("",colored.fg("light_green_2"))
print ("   ___       _   _                     ___                         ___           _     _               ")
print ("  / _ \_   _| |_| |__   ___  _ __     / _ \_ __ _____  ___   _    / _ \_ __ __ _| |__ | |__   ___ _ __ ")
print (" / /_)/ | | | __| '_ \ / _ \| '_ \   / /_)/ '__/ _ \ \/ / | | |  / /_\/ '__/ _` | '_ \| '_ \ / _ \ '__|")
print ("/ ___/| |_| | |_| | | | (_) | | | | / ___/| | | (_) >  <| |_| | / /_\\| | | (_| | |_) | |_) |  __/ |  ")
print ("\/     \__, |\__|_| |_|\___/|_| |_| \/    |_|  \___/_/\_\\__, | \____/|_|  \__,_|_.__/|_.__/ \___|_|   ")
print ("       |___/                                             |___/                                         ")
print ("",colored.fg("purple_4a"))
print ("                                                                                    GiulDZN#1337       ")
print ("                                                                                          for CrashedDevelopment       ")
time.sleep(5)
#here comes a little loading animation to make it not that borin lul
os.system("cls") #windows
#os.system("clear")  (Linux - OSX)
print ("",colored.fg("sky_blue_1"))
print ("loading [\]")
time.sleep(1)
os.system("cls") #windows
#os.system("clear")  (Linux - OSX)
print ("loading [|]")
time.sleep(1)
os.system("cls") #windows
#os.system("clear")  (Linux - OSX)
print ("loading [/]")
time.sleep(1)
os.system("cls") #windows
#os.system("clear")  (Linux - OSX)
print ("loading [-]")
time.sleep(1)
os.system("cls") #windows
#os.system("clear")  (Linux - OSX)
url = 'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all' #requests api url
r = requests.get(url)

with open('proxys.txt', 'wb') as f:  #saves as txt in current dir
    f.write(r.content)

print ("Sucessfully grabbed Proxys UwU")
print ("Proxy file is located in you current directory")

    
