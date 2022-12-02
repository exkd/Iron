from rich.console import Console
from rich.table import Table

from gtts import gTTS

import pyautogui

import time

table = Table(title=" ")
console = Console()

ascii_logo = [
    "                                                    ",
    " _|_|_|      _|_|_|          _|_|        _|      _|  ",
    "   _|        _|    _|      _|    _|      _|_|    _|  ",
    "   _|        _|_|_|        _|    _|      _|  _|  _|  ",
    "   _|        _|    _|      _|    _|      _|    _|_|  ",
    " _|_|_|      _|    _|        _|_|        _|      _|  "
]

main_menu = [
    "Text To Speech",
    "Auto Clicker",
    "Credits",
]

def display_logo():
    i = 0

    for line in ascii_logo:
        if i == 0:
            print(line)
            i = i + 1
        elif i == 1 or i == 2:
            console.print(line, style="red")
            i = i + 1
        elif i == 3 or i == 4:
            console.print(line, style="blue")
            i = i + 1
        elif i == 5:
            console.print(line, style="green")

def create_menu(menu):
    counter = 1

    for i in menu:
        print(f"{counter}. {i}")

        counter += 1
    
    return (int(input("Choose an item : ")))

def tts():
    text = input("Enter text: ")
    lang = input("Enter lang(ex.en): ")
    name = input("Enter file name/path: ")
    slow = bool(input("Slow? (true/false): "))


    audio = gTTS(text=text, lang=lang, slow=slow)
    audio.save(name)

def autoclicker():
    wait = input("Enter time to start autoclick (seconds) : ")
    click_amount = input("Enter amount of clicks : ")

    time.sleep(int(wait))

    for i in range(int(click_amount)):
        pyautogui.click()

def credits():
    print("Made by Mohammed Daniyal.")
    input(": ")

def start():
    while True:
        display_logo()

        print("")

        option_index = create_menu(main_menu)
        option_index = int(option_index) - 1

        if option_index == 0:
            tts()

        elif option_index == 1:
            autoclicker()

        elif option_index == 2:
            credits()

start()