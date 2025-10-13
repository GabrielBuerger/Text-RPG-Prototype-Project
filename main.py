from player import Player
from characters import *
from character_creation import character_creation
from settings import *
from battle import *
from saving import *

text = str("""This is an example of text""")

run = bool(True)
menu = bool(True)
play = bool(True)
player1 = Player()
My_party = Player_party(player1)
# party.add_member(haruki)

current_loc = "Goldenrod town: Ramiel Hospital"

while run: #main loop
    while menu == True:
        clear()
        print("GAME TITLE")
        line("=", 22)
        print('''    >1 New game
    >2 Load game
    >3 Options
    >4 Quit''')
        line("=", 22)
        choice = str(input("> "))
        if choice == "1": 
            clear()
            choice = bool(overwritting(player1))
            if choice == True:
                name, stenghth, mind, agility, inteligence, spirit, charisma, luck = character_creation()
                player1 = Player(name, stenghth, mind, agility, inteligence, spirit, charisma, luck, current_loc)
                save(player1)
                clear()
                play = True
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

    while play: #game loop
        print_dialogue(player1, text)
        if current_loc == loonie.current_loc:
            Status.set_status(player1, 'bleed', 3)
            Status.set_status(player1, 'insanity', 9)
            enemies = Party((loonie, haruki))
            Battle(My_party, enemies)
        if current_loc == haruki.current_loc:
            Battle(Party, haruki)
        clear()
        line()
        character_menu(player1)
        print(f'''You are in {player1.current_loc}
    >0 Menu
    >1 Go somewhere''')
        line()
        choice = str(input("> "))
        if choice == "0":
            clear()
            menu, play = True, False
        elif choice == "1":
            line()
            player1.move(current_location=current_loc)
            current_loc = player1.current_loc
            clear()
        elif choice == "2":
            player1.add_inventory("potion")
            player1.check_inventory()
            input()
