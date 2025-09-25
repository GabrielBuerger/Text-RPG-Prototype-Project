import os

def clear():
    os.system("cls")

def character_menu(name):
    print(f"{name.name} HP:[{name.max_hp}/{name.current_hp}] Mana:[{name.max_mana}/{name.mana}]")

def line(line:str="-", size:int=20):
    print(line*size)
