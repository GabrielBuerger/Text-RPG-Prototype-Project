from character_base import Character
from time import sleep
from settings import *

class Team():
    def __init__(self, character1:Character,
                 character2:Character=None, 
                 character3:Character=None,
                 character4:Character=None):
        self.p1 = character1
        self.p2 = character2
        self.p3 = character3
        self.p4 = character4
        self.alive = bool(False)
        if self.p1.alive == False and self.p2.alive == False and self.p3.alive == False and self.p4.alive == False:
            self.alive = bool(False)

def turn(party:Character, enemies:Character):
    print(f"{party.name}'s turn")
    line()
    character_menu(party)
    character_menu(enemies)
    line()
    party.action(enemies)
    if party.actions > 1:
        print('Quick feet! You have one more action.')
        party.action(enemies)
    input()
    clear()

def round(party:Character, enemies:Character):
    turn_order = list()
    turn_order.append(party)
    turn_order.append(enemies)
    for character_turn in range(0, len(turn_order)):
        if turn_order[character_turn] == party:
            turn(turn_order[character_turn], enemies)
        elif turn_order[character_turn] == enemies:
            turn(turn_order[character_turn], party)
    party.round_status()

def Battle (party:Character, enemies:Character):
    battle = bool(True)
    while battle:
        round(party=party, enemies=enemies)
        if party.alive == False:
            print('You died.')
            break
        elif enemies.alive == False:
            print('You won!')
            break
        else:
            pass
