from character_base import Character
from random import randint

class NPC(Character):
    def __init__(self, name, strenght, mind, agility, inteligence, luck, current_loc:str="Void"):
        super().__init__(name, strenght, mind, agility, inteligence, luck, current_loc)
