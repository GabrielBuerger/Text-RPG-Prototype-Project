from time import sleep
from settings import *
from status import *
from team import Enemy_party, Player_party, Character

def turn(character:Character, enemies:Enemy_party|Player_party|Character, allies:Player_party|Enemy_party=None):
    print(f"{character.name}'s turn")
    line()
    character_menu(character)
    line()
    print('''1> Action
2> Check
3> Inventory
4> Run''')
    line()
    choice = input("> ")
    clear()
    if choice == '1':
        character.action(enemies)
    if character.actions > 1:
        print('Quick feet! You have one more action.')
        turn(character=character, allies=allies, enemies=enemies)
    input()
    status.process_status(character)
    clear()
    battle = win_cond()
    return battle

def round(player_side:Player_party|Character, enemy_side:Enemy_party|Character):
    turn_order = list()
    if isinstance(player_side,Player_party):
        for character in range(0,len(player_side.members)):
            turn_order.append(player_side.members[character])
    else:
        turn_order.append(player_side)
    if isinstance(enemy_side, Enemy_party):
        for character in range(0, len(enemy_side.members)):
            turn_order.append(enemy_side.members[character])
    else:
        turn_order.append(enemy_side)
    input()
    for character in range(0, len(turn_order)):
        if isinstance(turn_order[character],Player_party|Enemy_party):
            if turn_order[character] in player_side.members:
                battle = turn(turn_order[character], enemy_side, player_side)
            else:
                battle = turn(turn_order[character], player_side, enemy_side)
        elif isinstance(turn_order[character],Character):
            if turn_order[character] in player_side.members:
                battle = turn(turn_order[character], enemy_side)
            else:
                battle = turn(turn_order[character], player_side)
        status.process_status(turn_order[character], "rbe")
        return battle

def Battle (player_side:Player_party|Character, enemy_side:Enemy_party|Character):
    print("BATTLE AHEAD!")
    sleep(2)
    battle = bool(True)
    while battle:
        battle = round(player_side=player_side, enemy_side=enemy_side)

def win_cond(player_side:Player_party|Character, enemy_side:Enemy_party|Character):
    if (player_side == Character and player_side.alive == False) or (player_side == Player_party and player_side.alive == False):
        print('You died.')
        return False
    elif (enemy_side == Character and enemy_side.alive == False) or (enemy_side == Player_party and enemy_side.alive == False):
        print('You won!')
        return False
    else:
        pass
