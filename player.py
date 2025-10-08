from character_base import Character
from map import map

class Player(Character):
    def __init__(self, name='Unk', strenght='0', mind='0', agility='0', inteligence='0', spirit='0', luck=0, charisma='0', current_loc:str="Void"):
        super().__init__(name, strenght, mind, agility, inteligence, spirit, charisma, luck, current_loc)
    def turn(self, target:Character=None, actions:int=1):
        print("""
>1 Basic attack
>2 Defend
>3 Atack skills
>4 special skills""")
        select = input(">")
        if select == "1":
            self.basic_attack(target)
            print(f"{target.name} taked {self.damage} damage")
            actions -=1
        elif select == "2" and self.mana < 8:
            print("You've run out of mana, you can't perform a magical attack")
        elif select == "2":
            self.magic_attack(target)
            print(f"{target.name} taked {self.magical_damage} from magical damage")
            print(f"Mana:[{self.max_mana}/{self.mana}]")
            actions -=1
        else:
            print("Invalid input. Please, insert again.")
    def move(self, current_location):
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
        return new_location
