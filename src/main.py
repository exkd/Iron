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
    "1. Text To Speech",
    "2. Auto Clicker",
    "3. Credits"
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

def create_menu(number_of_columns, menu):
    for i in range(number_of_columns):
        table.add_column("                           ", justify="left", style="cyan", no_wrap=True)

    multiple = len(menu) / number_of_columns
    multiple = int(multiple)

    counter = 1

    for i in range(number_of_columns):

        # print(counter, counter + number_of_columns, (counter + number_of_columns)+number_of_columns)
        table.add_row(menu[counter - 1], menu[counter + number_of_columns - 1], menu[(counter + number_of_columns)+number_of_columns - 1])

        counter += 1
    
    console.print(table)

    return int(input("Choose an option: ")) - 1

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

        option_index = create_menu(1, main_menu)
        option_index = int(option_index)

        if option_index == 0:
            tts()

        elif option_index == 1:
            autoclicker()
        
        elif option_index == 2:
            credits()

start()