from player import Player

def save(player=Player):
    # file=open("load.txt", "a")
    saving = dict()
    arc = str("data.txt")
    with open(arc, "w") as file:
        for attr, val in player.__dict__.items():
            saving[attr] = str(val)
            file.write(str((attr)+'\n'+str((val))+'\n'))
    # file.close()

def load(player:Player):
    arc = str("data.txt")
    with open(arc, "r") as file:
        lines = list()
        for line in file.readlines():
           lines.append(line.strip("\n"))
    for i in range(0, len(lines), 2):
        key = str(lines[i])
        value = str(lines[i+1])
        if value.isnumeric():
            value = int(value)
        setattr(player, str(key), value)

def overwritting(player:Player):
    try:
        with open("data.txt", 'r') as file:
            choice = int()
            load(player)
            while True:
                print("Are you sure you want to overwrite your last save? ")
                print('''    >1 Yes
    >2 No
''')
                choice = str(input("> "))
                if choice == "1":
                    return True
                elif choice == "2":
                    return False
                else:
                    print("Invalid output")
    except:
        return True