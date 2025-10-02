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
    with open(arc, "r") as f:
        lines = list()
        for line in f.readlines():
           lines.append(line.strip("\n"))
    for i in range(0, len(lines), 2):
        key = str(lines[i])
        value = str(lines[i+1])
        if value.isnumeric():
            value = int(value)
        setattr(player, str(key), value)

# saving.py (CHAT GPT solution ongoing studies...)

# from player import Player



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
