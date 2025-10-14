from time import sleep
from settings import *
from status_base import *
from team import Party, Player_party
from player import Player, Character
from random import randint

# (Battle loop -> Round -> Turn) * win_condition

def win_cond(player_side:Player_party|Character, enemy_side:Party|Character):
    if player_side.alive == False:
        input('You died.')
        return False
    elif enemy_side.alive == False:
        input('You won!')
        return False
    else:
        return True
    

def Battle (player_side:Player_party, 
            enemy_side:Party):
# Battle menu
    characters = list()
    print("BATTLE AHEAD!")
    input()
    clear()
    print("Your party:")
    if len(player_side.members) > 1:
        for character in range(0, len(player_side.members)):
            print("     >", str((player_side.members[character]).name))
            characters.append(player_side.members[character])
    elif len(player_side.members) == 1:
        print("     >", player_side.members[0].name)
        characters.append(player_side.members[0])
    print("             VS")
    if len(enemy_side.members) > 1:
        for character in range(0, len(enemy_side.members)):
            print("     >", str((enemy_side.members[character]).name))
            characters.append(enemy_side.members[character])
    elif len(enemy_side.members) == 1:
        print("     >", enemy_side.members[0].name)
        characters.append(enemy_side.members[0])
    input()
# Main battle loop
    battle = bool(True)
    while battle:
        round(player_side, enemy_side, characters)
        battle = win_cond(player_side, enemy_side)


def round(player_side:Player_party, 
          enemy_side:Party, 
          turn_order:list):
# turn order organizing
# Characters' turns
    for character in range(0, len(turn_order)):
        #if you have a party, if character is you
        if (len(player_side.members) > 1) and (turn_order[character] in player_side.members):
            turn(turn_order[character], enemy_side, player_side)
        
        #if enemies have their party, if character is your enemy
        elif (len(enemy_side.members) > 1) and (turn_order[character] in enemy_side.members):
            turn(turn_order[character], player_side, enemy_side)
        
        #if you, the player, do not have a party, if character is you
        elif (len(player_side.members) == 1) and (turn_order[character] in player_side.members):
            turn(turn_order[character], enemy_side)
        
        #if your enemy does not have a party, if character is your enemy
        elif (len(enemy_side.members) == 1) and (turn_order[character] in enemy_side.members):
            turn(turn_order[character], player_side)

        battle = win_cond(player_side, enemy_side)
        if battle == False:
            return battle


def turn(character:Character, 
         enemies:Party|Player_party, 
         allies:Player_party|Party=None):
    clear()
    print(f"{character.name}'s turn")
    line()
    character_menu(character)
    line()
    if isinstance(character,Player):
        while True:
            print('''Select action:
    1> Move
    2> Check info
    3> Inventory
    4> Run''')
            line()
            choice = str(input("> "))
            if str(choice).isnumeric() == False:
                input("Invalid input.")
                clear()
                continue
            elif str(choice) == '1':
                target = player_target(enemies)
                character.action(target)
                break
            elif str(choice) == "2":
                for enemy in range(0, len(enemies.members)):
                    character_menu(enemies.members[enemy])
                break
            else:
                input("Invalid input.")
                clear()
                continue
    else:
        target = NPC_target(enemies)
        character.action(target)
    if character.actions > 1:
        print(f'Quick feet! {character.name} have one more action.')
        turn(character=character, enemies=enemies, allies=allies)
    Status.proccess_status(character)
    character.inner_mind()
    input()


def player_target(enemies:Party):
    if len(enemies.members) > 1:
        while True:
            clear()
            line()
            print("Choose target: ")
            for c in range(0, len(enemies.members)):
                print(f"    >{c+1} {enemies.members[c].name}")
            # if shadows == Party:
            #     for s in range(c, len(shadows.members)):
            #         print(f"    >{s+1} {shadows.members[s].name}")           
            line()
            choice = str(input("> "))
            if str(choice).isnumeric() == False:
                input("Invalid input.")
                clear()
                continue
            if int(choice) > len(enemies.members) or int(choice) < 1:
                input("Invalid input.") 
                clear()
                continue
            for c in range(0, len(enemies.members)):
                if int(choice)-1 == c:
                    clear()
                    return enemies.members[int(choice)-1]
            break
    elif len(enemies.members) == 1:
        return enemies.members[0]
    # elif isinstance(enemies, Character) and shadows == Party:
    #     for s in range(0, len(shadows.members)):
    #         print(f"    >{s+1} {shadows.members[s].name}") 

def NPC_target(enemies: Player_party):
    if len(enemies.members) > 1:
        choice = randint(0, len(enemies.members))
        for c in range(0, len(enemies.members)):
            if choice == c:
                return enemies.members[c]
    elif len(enemies.members) == 1:
        return enemies.members[0]
    # elif isinstance(enemies, Character) and shadows == Party:
    #     for s in range(0, len(shadows.members)):
    #         print(f"    >{s+1} {shadows.members[s].name}") 
