from character_base import*
from setups import*
from time import sleep
from characters import*
from saving import*
from character_creation import *

run = bool(True)
menu = bool(True)
battle = bool(True)

while run == True:
    while menu == True:
        clear()
        print(20*"=", '''
>1 New game
>2 Load game
>3 Options
>4 Quit
''', 
20*"=")
        choice = str(input("> "))
        if choice == "1":
            name, stenghth, mind, agility, inteligence, luck = character_creation()
            player1 = Player(name, stenghth, mind, agility, inteligence, luck)
            save(player1)
            battle = True
            menu = False
        elif choice == "2":
            try:
                load(player1)
            except:
                input("ERROR: There's no data saved, please create a new game.\n\n>")
                continue
            battle = True
            menu = False
        elif choice == "3":
            pass
        elif choice == "4":
            quit()
        else:
            print("Invalid input")
    clear()
    while battle == True:
        line()
        character_menu(player1)
        character_menu(loonie)
        line()
        if player1.current_hp == 0 or loonie.current_hp == 0:
            battle = False
            break   
        print(f"{player1.name}'s turn")
        print("""
    >1 Physical Attack
    >2 Magical attack
            """)
        player1.action(loonie)
        sleep(2)
        clear()
        line()
        character_menu(player1)
        character_menu(loonie)
        line()
        input("Enter to continue...")
        print(f"{loonie.name}'s turn")
        sleep(2)
        loonie.action(player1)
        sleep(2)
        clear()
    run = False
