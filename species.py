from character_base import Character
from random import uniform

class Fox (Character):
    def __init__(self, name:str, strenght:int, mind:int, agility:int, intelect:int, spirituality:int, charisma:int, current_loc:str):
        super().__init__(name, strenght, mind, agility, intelect, spirituality, charisma, current_loc)
    def quick_feet(self:Character):
        self.actions = int(2)
    def aware(self:Character):
        self.speed = int(float(self.speed)*(0.75))


