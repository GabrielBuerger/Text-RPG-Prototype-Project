from character_base import Player

def save(character):
    # file=open("load.txt", "a")
    saving = list()
    with open("load.txt", "w") as file:
        for attribute, value in character.__dict__.items():
            saving.append(str(attribute))
            saving.append(str(value))
        for item in saving:
            file.write(item + "\n")
    # file.close()

def load(player=Player):
    attr = list()
    vals = list()
    c = int(0)
    with open("load.txt", "r") as file:
        for line in file:
            c += 1
            #odd nums = objects atributes
            if float(c % 2 != 0):
                attr.append(line.strip("\n"))
            #even nums = atribute values
            else:
                vals.append(line.strip("\n"))
                if vals[-1].isnumeric() == True:
                    vals[-1] = int(vals[-1])
                setattr(player, attr[-1], vals[-1])
                print(attr[-1], "=", vals[-1])
