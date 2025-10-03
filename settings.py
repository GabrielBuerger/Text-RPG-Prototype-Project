import os
from player import Player

# class array():
#     def __init__(self, *args):
#         array = list()

def clear():
    os.system("cls")

def character_menu(name:Player):
    print(f"{name.name} HP:[{name.max_hp}/{name.current_hp}] Mana:[{name.max_mana}/{name.mana}]")

def line(line:str="-", size:int=20):
    print(line*size)
