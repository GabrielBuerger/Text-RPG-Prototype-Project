from settings import clear, line

def character_creation():
    name = str(input("Insert your name: \n> "))
    str_pts = mind_pts = agi_pts = int_pts = luc_pts = int(1)
    init_maxpts = int(10)
    max_pts = int(init_maxpts)
    while True:
        clear()
        line()
        print(f'''REMAINING POINTS = {max_pts}
1> Strenght: {str_pts}
2> Mind: {mind_pts}
3> Agility: {agi_pts}
4> Inteligence: {int_pts}
5> Luck: {luc_pts}''')
        line()
        if max_pts == 0:
            print('''Are you sure you want to continue?
1> Save
2> Reset''')
            line()
            choice = str(input("> "))
            if choice == "1":
                break
            elif choice == "2":
                str_pts = mind_pts = agi_pts = int_pts = luc_pts = int(1)
                max_pts = int(init_maxpts)
                continue
            else:
                input("Invalid input ")
        choice = str(input("> "))
        if choice == "1":
            str_pts +=1
            max_pts -=1
        elif choice == "2":
            mind_pts +=1
            max_pts -=1
        elif choice == "3":
            agi_pts +=1
            max_pts -=1
        elif choice == "4":
            int_pts +=1
            max_pts -=1
        elif choice == "5":
            luc_pts +=1
            max_pts -=1
        else:
            input("Invalid input ")
    return name, str_pts, mind_pts, agi_pts, int_pts, luc_pts
