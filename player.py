from character_base import Character
from map import map
from settings import line

class Player(Character):
    def __init__(self, name='Unk', strenght='0', mind='0', agility='0', inteligence='0', spirit='0', luck=0, charisma='0', current_loc:str="Void"):
        super().__init__(name, strenght, mind, agility, inteligence, spirit, charisma, luck, current_loc)
    def action(self, target:Character):
        line()
        print("""Chose your move
    >1 Basic attack
    >2 Defend
    >3 Atack skills
    >4 special skills""")
        line()
        select = input("> ")
        line()
        if select == "1":
            self.basic_attack(target)
            print(f"{target.name} took {self.physical_damage} damage")
        elif select == "2" and self.mana < 8:
            print("You've run out of mana, you can't perform a magical attack")
        elif select == "2":
            self.magic_attack(target)
            print(f"{target.name} took {self.magical_damage} from magical damage")
            print(f"Mana:[{self.max_mana}/{self.mana}]")
        else:
            print("Invalid input.")
    def move(self, current_location):
        c = int()
        places = list()
        for direction in map[current_location]:
            c += 1
            places.append(map[current_location][direction])
            print(f'    >{c} {direction} ({places[c-1]})')
        while True:
            print("Please insert the direction: ")
            choice = input(str("> "))
            if choice.isnumeric() == False:
                print("invalid comand")
            elif int(choice) > c or int(choice) < 1:
                print("invalid comand")
            elif places[int(choice)-1] in map:
                new_location = str(places[int(choice)-1])
                setattr(self,"current_loc", new_location)
                break
            else:
                print("invalid comand")
        return new_location
