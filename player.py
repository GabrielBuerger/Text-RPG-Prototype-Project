from character_base import Character
from map import map
from settings import clear

class Player(Character):
    def __init__(self, name, strenght, mind, agility, inteligence, luck, current_loc:str="Void"):
        super().__init__(name, strenght, mind, agility, inteligence, luck, current_loc)
    def action(self, target=None):
        while True:
            select = input(">")
            if select == "1":
                self.physical_attack(target)
                print(f"{target.name} taked {self.damage} damage")
                break
            elif select == "2" and self.mana < 8:
                print("You've run out of mana, you can't perform a magical attack")
            elif select == "2":
                self.magic_attack(target)
                print(f"{target.name} taked {self.magic_damage} from magical damage")
                print(f"Mana:[{self.max_mana}/{self.mana}]")
                break
            else:
                print("Invalid input. Please, insert again.")
    def move(current_location):
        self = Player
        current_location = getattr(self, "current_loc")
        c = int()
        places = list()
        for direction in map[current_location]:
            c += 1
            places.append(map[current_location][direction])
            print(f'>{c} {direction} ({places[c-1]})')
        while True:
            choice = input(str("Please insert the direction: > "))
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
        clear()
        return new_location
