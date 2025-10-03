from character_base import Character
from random import randint

class NPC(Character):
    def __init__(self, name, strenght, mind, agility, inteligence, luck, current_loc:str="Void"):
        super().__init__(name, strenght, mind, agility, inteligence, luck, current_loc)
    def turn(self, target:Character=None, actions:int=1):
        while actions != 0:
            select = str(randint(1,2))
            if select == "1":
                self.basic_attack(target)
                print(f"{target.name} taked {self.damage} damage")
                break
            elif select == "2" and self.mana < 8:
                pass
            elif select == "2":
                self.magic_attack(target)
                print(f"{target.name} taked {self.magical_damage} from magical damage")
                print(f"Mana:[{self.max_mana}/{self.mana}]")
                break
