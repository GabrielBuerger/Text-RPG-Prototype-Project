import os
from character_base import Character

def clear():
    os.system("cls")

def character_menu(character:'Character'):
    print(f"{character.name} HP:[{character.max_hp}/{character.hp}] Mana:[{character.max_mana}/{character.mana}]")
    print('Status:', end=' ')
    if not character.status:
        print('None', end='\n')
        return
    c = 0
    for status in character.status:
        c += 1
        if len(character.status) == c:
            print(status, f'({character.status[status]})', end='.\n')
        else:
            print(status, f'({character.status[status]})', end='; ')
            
def line(line:str="-", size:int=20):
    print(line*size)

def print_dialogue(speaker:Character, text:str="..."):
    line()
    print(f"{speaker.name}: ")
    print(text)
    line()
    input("> ")