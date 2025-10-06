import os
from character_base import Character

# class array():
#     def __init__(self, *args):
#         array = list()

def clear():
    os.system("cls")

def character_menu(character:'Character'):
    print(f"{character.name} HP:[{character.max_hp}/{character.current_hp}] Mana:[{character.max_mana}/{character.mana}]")
    print('Status:', character.status)
def line(line:str="-", size:int=20):
    print(line*size)
