from character_class import Character
from random import random

class NPC(Character):
    def __init__(self, name, strenght, mind, agility, inteligence, luck, current_loc:str="Void"):
        super().__init__(name, strenght, mind, agility, inteligence, luck, current_loc)
    def action(self,target):
        while True:
            select = str(random.randint(1,2))
            if select == "1":
                self.physical_attack(target)
                print(f"{target.name} taked {self.damage} damage")
                break
            elif select == "2" and self.mana < 8:
                pass
            elif select == "2":
                self.magic_attack(target)
                print(f"{target.name} taked {self.magic_damage} from magical damage")
                print(f"Mana:[{self.max_mana}/{self.mana}]")
                break
