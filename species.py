from character_base import Character
from random import uniform

class Fox (Character):
    def __init__(self):
        pass
    def quick_feet(self:Character):
        self.actions = int(2)
    def aware(self:Character):
        self.speed = int(float(self.speed)*(0.75))


