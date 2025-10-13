from character_base import Character

class Shadow(Character):
    def __init__(self, name, target, strenght, mind, agility, intelect, spirituality, charisma, luck, current_loc):
        super().__init__(name, strenght, mind, agility, intelect, spirituality, charisma, luck, current_loc)
        self.target = target
    
