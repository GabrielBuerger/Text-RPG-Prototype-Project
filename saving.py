from player import Player

def save(player=Player):
    # file=open("load.txt", "a")
    saving = list()
    arc = str("data.txt")
    with open(arc, "w") as file:
        for attribute, value in player.__dict__.items():
            saving.append(str(attribute))
            saving.append(str(value))
        for item in saving:
            file.write(item + "\n")
    # file.close()

def load(player=Player):
    attr = list()
    vals = list()
    c = int(0)
    arc = str("data.txt")
    with open(arc, "r") as file:
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

# saving.py (CHAT GPT solution ongoing studies...)

# from player import Player

# def load():
#     with open("data.txt", "r") as f:
#         lines = [line.strip() for line in f.readlines()]

#     # Turn into dict (pairs of key/value)
#     save_data = {}
#     for i in range(0, len(lines), 2):
#         key = lines[i]
#         value = lines[i+1]
#         save_data[key] = value

#     # Create a new Player instance from saved stats
#     player = Player(
#         name=save_data["name"],
#         strenght=int(save_data["strenght"]),
#         mind=int(save_data["mind"]),
#         agility=int(save_data["agility"]),
#         inteligence=int(save_data["inteligence"]),
#         luck=int(save_data["luck"]),
#         current_loc=save_data["current_loc"]
#     )

#     # Restore current HP, mana, etc.
#     player.current_hp = int(save_data["current_hp"])
#     player.mana = int(save_data["mana"])
#     player.money = int(save_data["money"])
#     player.alive = save_data["alive"] == "True"
#     player.status = save_data["status"] == "True"

#     return player
