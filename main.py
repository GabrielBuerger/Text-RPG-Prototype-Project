from player import Player
from characters import *
from character_creation import character_creation
from settings import *
from battle import *
from saving import *

run = bool(True)
menu = bool(True)
play = bool(True)
player1 = Player()
party = Player_party(player1, (haruki))

current_loc = "Goldenrod town: Ramiel Hospital"

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
        name, stenghth, mind, agility, inteligence, spirit, charisma, luck = character_creation()
        player1 = Player(name, stenghth, mind, agility, inteligence, spirit, charisma, luck, current_loc)
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
        quit()
    else:
        print("Invalid input")
while play:
    if current_loc == loonie.current_loc:
        status.set_status(player1, 'bleed', 3)
        Battle(party, loonie)
    if current_loc == haruki.current_loc:
        Battle(party, haruki)
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
        menu, play = True, False
    elif choice == "1":
        player1.move(current_location=current_loc)
        current_loc = player1.current_loc
        clear()
    elif choice == "2":
        player1.check_inventory()
        input()
