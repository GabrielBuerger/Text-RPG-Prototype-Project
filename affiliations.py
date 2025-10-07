from character_base import Character
from random import uniform
from abc import abc

class The_Moon(abc):
    def children_of_the_Moon():
        pass
    def insanity_fueled():
        pass
    def crazy_strenght():
        pass

class The_Fox(abc):
    def violent_start(self:Character):
        self.rage = int(float(self.max_rage)*(0.4))
    def bloody_mess(self:Character, target:Character): 
        pass
    def basic_attack(self:Character, target:Character):
        super().basic_attack(target)
        bleeding = int(uniform(0,1))
        if bleeding < 0.2:
            target.set_status("bleed", 3)
    def violence():
        pass

