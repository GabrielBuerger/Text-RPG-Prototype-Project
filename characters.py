from character_base import Character
from species import *
from NPC import NPC
from affiliations import *

class Loonie(Character, Fox, The_Fox, The_Moon):
    def __init__(self, name, strenght, mind, agility, inteligence, luck, charisma, current_loc):
        super().__init__(name, strenght, mind, agility, inteligence, luck, charisma, current_loc)
    def chosen_by_the_moon():
        pass
    def bastard_son():
        pass
    def blood_doesnt_define():
        pass
    def fight_to_survive():
        pass
    def Loonies_a_lunatic():
        pass
    def used_to_run():
        pass
    def passionate():
        pass
    def flowery_boy():
        pass


loonie = Loonie(name="Loonie Hikashi",
                   strenght="4",
                   mind="1",
                   agility="7",
                   inteligence='7',
                   luck='1',
                   charisma='3',
                   current_loc="Mt.Silver"
                   )
haruki = Character(name="Haruki Hirasawa", 
                   strenght="2",
                   mind="1",
                   agility="7",
                   inteligence='5',
                   luck='7',
                   charisma='3',
                   current_loc="The Giant mushroom forest"
                   )
