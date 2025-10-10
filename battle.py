from time import sleep
from settings import *
from status import *
from team import Party, Player_party, NPC
from player import Player, Character
from random import randint

# Battle > Round > Turn 

def turn(character:Character, 
         enemies:Party|Player_party|Character, 
         allies:Player_party|Party|Character=None):
    print(f"{character.name}'s turn")
    line()
    character_menu(character)
    line()
    if isinstance(character,Player):
        print('''Select action:
    1> Move
    2> Check info
    3> Inventory
    4> Run''')
        line()
        choice = input("> ")
    else:
        choice = str(randint(1, 2))
    clear()
    if choice == '1':
        if isinstance (enemies, Party) and isinstance(character, Player):
            print("Chose target: ")
            for c in range(0, len(enemies.members)):
                print(f"    >{c+1} {enemies.members[c].name}")
            choice = str(input("> "))
            for c in range(0, len(enemies.members)):
                if int(choice)-1 == c:
                    clear()
                    character.action(enemies.members[int(choice)-1])
        elif isinstance(enemies, Party) and isinstance(character, NPC):
            choice = randint(0, len(enemies.members))
            for c in range(0, len(enemies.members)):
                if choice == c+1:
                    character.action(enemies.members[c])
        elif isinstance(enemies, Character) and isinstance(character, NPC):
           character.action(enemies)
        elif isinstance(enemies, Character) and isinstance(character, Player):
            character.action(enemies)
    elif choice == "2":
        for enemy in range(0, len(enemies.members)):
            character_menu(enemies.members[enemy])
    if character.actions > 1:
        print('Quick feet! You have one more action.')
        turn(character=character, enemies=enemies, allies=allies)
    status.process_status(character)


def round(player_side:Player_party|Character, enemy_side:Party|Character, turn_order:list):
# turn order organizing
# Characters' turns
    for character in range(0, len(turn_order)):
        if isinstance(turn_order[character], Player_party):
            turn(turn_order[character], enemy_side, player_side)
        elif isinstance(turn_order[character], Party):
            turn(turn_order[character], player_side, enemy_side)
        elif isinstance(turn_order[character], Character) and turn_order[character] in player_side.members:
            turn(turn_order[character], enemy_side)
        elif isinstance(turn_order[character], Character) and turn_order[character] in enemy_side.members:
            turn(turn_order[character], player_side)
        status.process_status(turn_order[character], "rbe")
        input()
        battle = win_cond(player_side, enemy_side)
        if battle == False:
            break


def Battle (player_side:Player_party|Character, enemy_side:Party|Character):
# Battle menu
    characters = list()
    print("BATTLE AHEAD!")
    input()
    clear()
    print("Your party:")
    if isinstance(player_side, Player_party):
        for character in range(0, len(player_side.members)):
            print("  >", str((player_side.members[character]).name))
            characters.append(player_side.members[character])
    elif isinstance(player_side, Character):
        print("  >", player_side.name)
        characters.append(player_side)
    print("          VS")
    if isinstance(enemy_side, Party):
        for character in range(0, len(enemy_side.members)):
            print("  >", str((enemy_side.members[character]).name))
            characters.append(enemy_side.members[character])
    elif isinstance(enemy_side, Character):
        print("  >", enemy_side.name)
        characters.append(enemy_side)
    input()
# Main battle loop
    battle = bool(True)
    while battle:
        round(player_side=player_side, enemy_side=enemy_side, turn_order=characters)
        battle = win_cond(player_side, enemy_side)

def win_cond(player_side:Player_party|Character, enemy_side:Party|Character):
    if player_side.alive == False:
        input('You died.')
        return False
    elif enemy_side.alive == False:
        input('You won!')
        return False
    else:
        return True
