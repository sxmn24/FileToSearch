import os
import pyfiglet
from turtle import end_fill
from pasek import Pasek
from os import get_terminal_size
from time import sleep
import time
from pasek import Pasek
from os import get_terminal_size
from time import sleep


class FindFile():
    print(pyfiglet.figlet_format("BETA 1.0\r  MADE BY SPIDI"))
    print("Welcome, If you don't see anything restart the program.")
    time.sleep(5)  
    
    
    print("Starting: ")
    # szerokość
    szerokosc = get_terminal_size()[0]

    # pasek
    pasek = Pasek(szerokosc=szerokosc / 2)
    for i in range (50):
        pasek.dalej(procent=i/50)
        sleep(0.2)
    pasek.koniec()

    rootDir = "C:\\"
    print("Napisz jaki plik chcesz znaleść: ")
    fileToSearch = input(" ")

    for relPath, dirs, files in os.walk(rootDir):
        if (fileToSearch in files):
            fullPath = os.path.join(rootDir, relPath, fileToSearch)
            print(fullPath)
            print("File is found")
            break
    else:
        print("File is not found")
        
FindFile
    
    
    