from settings import *
from player import Player
from NPC import NPC
from time import sleep

def battle(character1:Player, character2:NPC):
    while True:
        line()
        character_menu(character1)
        character_menu(character2)
        line()
        if character1.current_hp == 0:
            print(f"{character1.name} is defeated.")
            return
        elif character2.current_hp == 0:
            print(f"{character2.name} is defeated.")
            return
        print(f"{character1.name}'s turn")
        print("""
>1 Basic attack
>2 Defend
>3 Atack skills
>4 special skills
            """)
        character1.action(character2)
        sleep(2)
        clear()
        line()
        character_menu(character1)
        character_menu(character2)
        line()
        input("Enter to continue...")
        print(f"{character2.name}'s turn")
        sleep(2)
        character2.action(character1)
        sleep(2)
        clear()
