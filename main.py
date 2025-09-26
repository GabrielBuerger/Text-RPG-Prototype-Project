from character_base import *
from setups import *
from time import sleep
from characters import *

run = bool(True)
menu = bool(True)
battle = bool(True)

current_loc = "Goldenrod town: Ramiel Hospital"

while run == True:
    while menu == True:
        clear()
        print(20*"=", '''
>1 Play
>2 Options
>3 Quit
''', 
20*"=")
        choice = str(input("> "))
        if choice == "1":
            name = str(input("Insert your name: \n>"))
            player1 = Player(name=name, strenght=5, mind=5, agility=5, inteligence=5, luck=5, spirit=5, current_loc=current_loc)
            battle = True
            menu = False
        elif choice == "2":
            pass
        elif choice == "3":
            quit()
        else:
            print("Invalid input")
    while True:
        clear()
        dest = str(input(f'''
        >0 Menu
        >1 Go to
        You are in {current_loc}
        '''))
        if dest == "0":
            menu = True
            play = False
            break
        if dest == "1":
            c = int()
            for i in map[current_loc]:
                c += 1
                print(f'>{c} {i}')
            while True:
                direction = input(str("Please insert the direction: "))
                if direction in map[current_loc]:
                    break
                else:
                    print("invalid comand")

            player1.move(current_location=current_loc, direction=direction)
            clear()
    while battle == True:
        line()
        character_menu(haruki)
        character_menu(loonie)
        line()
        if haruki.current_hp == 0 or loonie.current_hp == 0:
            battle = False
            break   
        print(f"{haruki.name}'s turn")
        print("""
    >1 Physical Attack
    >2 Magical attack
            """)
        haruki.action(loonie)
        sleep(5)
        clear()
        line()
        character_menu(haruki)
        character_menu(loonie)
        line()
        print(f"{loonie.name}'s turn")
        loonie.action(haruki)
        sleep(5)
        clear()
    run = False
