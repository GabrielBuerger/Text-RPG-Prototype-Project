from settings import *
from player import Player
from NPC import NPC
from time import sleep

def battle(character1:Player, character2:NPC):
    while character1.alive==True or character2.alive==True:
        if character1.current_hp == 0:
            print(f"{character1.name} is defeated.")
            return
        elif character2.current_hp == 0:
            print(f"{character2.name} is defeated.")
            return    
        line()
        character_menu(character1)
        character_menu(character2)
        line()
        character1.turn(character2)
        sleep(2)
        clear()
        line()
        character_menu(character1)
        character_menu(character2)
        line()
        input("Enter to continue...")
        print(f"{character2.name}'s turn")
        sleep(2)
        character2.turn(character1)
        sleep(2)
        clear()
