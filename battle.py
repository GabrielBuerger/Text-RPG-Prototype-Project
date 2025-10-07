from character_base import Character
from time import sleep
from settings import *
from team import Team, Party

def turn(character:Character, enemies:Team):
    print(f"{character.name}'s turn")
    line()
    character_menu(character)
    character_menu(enemies)
    line()
    character.action(enemies)
    if character.actions > 1:
        print('Quick feet! You have one more action.')
        character.action(enemies)
    input()
    clear()

def round(party:Party, enemies:Team):
    turn_order = list()
    turn_order.append(party)
    turn_order.append(enemies)
    for character_turn in range(0, len(turn_order)):
        if turn_order[character_turn] == party:
            turn(turn_order[character_turn], enemies)
        elif turn_order[character_turn] == enemies:
            turn(turn_order[character_turn], party)
    party.round_status()

def Battle (party:Party, enemies:Team):
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
