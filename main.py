from character_base import*
from setups import*
from time import sleep
from characters import*
from saves import*

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
            name = str(input("Insert your name: \n>"))
            player1 = Player(name=name, strenght=5, mind=5, agility=5, inteligence=5, luck=5, spirit=5)
            save(player1)
            battle = True
            menu = False
        elif choice == "2":
            load()
        elif choice == "3":
            pass
        elif choice == "4":
            quit()
        else:
            print("Invalid input")

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
