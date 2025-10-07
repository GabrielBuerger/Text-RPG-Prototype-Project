from settings import *

def base_stats():
    str_pts = mind_pts = agi_pts = int_pts = luc_pts = char_pts = int(1)
    max_pts = int(15)
    return(str_pts, mind_pts, agi_pts, int_pts, luc_pts, char_pts, max_pts)

def save_character(str_pts, mind_pts, agi_pts, int_pts, luc_pts, char_pts, max_pts):
    while True:
        print('''Are you sure you want to continue?
1> Save
2> Reset''')
        line()
        choice = str(input("> "))
        if choice == "1":
            return (False)
        elif choice == "2":
            base_stats()
            return(True)
        else:
            input("Invalid input ")

def character_creation():
    name = str(input("Insert your name: \n> "))
    stats = list(base_stats())
    creating = bool(True)
    while creating:
        clear()
        line()
        print(f'''REMAINING POINTS = {stats[7]}
1> Strenght: {stats[1]}
2> Mind: {stats[2]}
3> Agility: {stats[3]}
4> Inteligence: {stats[4]}
5> Luck: {stats[5]}
6> Charisma: {stats[6]}''')
        line()
        if stats[7] == 0:
            creating = save_character(stats[1], stats[2], stats[3], stats[4], stats[5], stats[6], stats[7])
        choice = str(input("> "))
        if choice == "1":
            stats[1] +=1
            stats[7] -=1
        elif choice == "2":
            stats[2] +=1
            stats[7] -=1
        elif choice == "3":
            stats[3] +=1
            stats[7] -=1
        elif choice == "4":
            stats[4] +=1
            stats[7] -=1
        elif choice == "5":
            stats[5] +=1
            stats[7] -=1
        elif choice == "6":
            stats[6] += 1
        else:
            input("Invalid input ")
    return name, stats[1], stats[2], stats[3], stats[4], stats[5]
