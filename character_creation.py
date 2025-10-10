from settings import *

def base_stats():
    str_pts = mind_pts = agi_pts = int_pts = spi_pts = char_pts, luc_pts = int(1)
    max_pts = int(15)
    return list(max_pts, str_pts, mind_pts, agi_pts, int_pts, spi_pts, char_pts, luc_pts)

def save_character(stats:list):
    while True:
        print('''Are you sure you want to continue?
1> Save
2> Reset''')
        line()
        choice = str(input("> "))
        if choice == "1":
            return (False, stats)
        elif choice == "2":
            stats.clear()
            stats = base_stats()
            return(True, stats)
        else:
            input("Invalid input ")

def character_creation():
    name = str(input("Insert your name: \n> "))
    stats = base_stats()
    creating = bool(True)
    while creating:
        clear()
        line()
        print(f'''REMAINING POINTS = {stats[0]}
1> Strenght: {stats[1]}
2> Mind: {stats[2]}
3> Agility: {stats[3]}
4> Intelect: {stats[4]}
5> Spirituality: {stats[5]}
6> Charisma: {stats[6]}
7> Luck: {stats[7]}''')
        line()
        if stats[0] == 0:
            creating, stats = save_character(stats=stats)
            continue
        choice = str(input("> "))
        if choice == "1": #Strenght
            stats[1] +=1
            stats[0] -=1
        elif choice == "2": #Mind
            stats[2] +=1
            stats[0] -=1
        elif choice == "3": #Agility
            stats[3] +=1
            stats[0] -=1
        elif choice == "4": # Inteligence
            stats[4] +=1
            stats[0] -=1
        elif choice == "5": # Spirituality
            stats[5] +=1
            stats[0] -=1
        elif choice == "6": # Charisma
            stats[6] += 1
            stats[0] -=1
        elif choice == "7": # Luck
            stats[7] += 1
            stats[0] -=1
        else:
            input("Invalid input ")
    return (str(name), 
            int(stats[1]), #Strengh
            int(stats[2]), #Mind
            int(stats[3]), #Agility
            int(stats[4]), #Intelect
            int(stats[5]), #Spirituality
            int(stats[6]), #Charisma
            int(stats[7])) #Luck
