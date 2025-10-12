import os
from character_base import Character

def clear():
    os.system("cls")

def character_menu(character:'Character'):
    print(f"{character.name} HP:[{character.max_hp}/{character.hp}] Mana:[{character.max_mana}/{character.mana}]")
    print('Status:', character.status)
def line(line:str="-", size:int=20):
    print(line*size)

def print_dialogue(speaker:Character, text:str="..."):
    line()
    print(f"{speaker.name}: ")
    print(text)
    line()
    input("> ")