from player import Player
from characters import *
from character_creation import character_creation
from settings import *
from battle import Team, Party, Battle
from saving import *

run = bool(True)
menu = bool(True)
play = bool(True)
player1 = Player()
party = Party(player1, (haruki))

current_loc = "Goldenrod town: Ramiel Hospital"

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
            player1 = Player(name, stenghth, mind, agility, inteligence, luck, current_loc)
            save(player1)
            menu = False
        elif choice == "2":
            try:
                load(player1)
            except:
                input("ERROR: There's no data saved, please create a new game.\n\n>")
                continue
            menu = False
        elif choice == "3":
            pass
        elif choice == "4":
            run = False
            quit()
        else:
            print("Invalid input")
    while play:
        if current_loc == loonie.current_loc:
            player1.set_status('bleed',3)
            Battle((player1), (loonie))
        if current_loc == haruki.current_loc:
            Battle(player1, haruki)
        clear()
        line()
        character_menu(player1)
        print(f'''You are in {player1.current_loc}
>0 Menu
>1 Go somewhere''')
        print(current_loc)
        line()
        choice = str(input("> "))
        if choice == "0":
            menu = True
            play = False
            break
        elif choice == "1":
            player1.move(current_location=current_loc)
            current_loc = player1.current_loc
            clear()
        elif choice == "2":
            player1.check_inventory()
            input()
