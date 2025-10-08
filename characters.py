from species import *
from affiliations import *

class Loonie(Fox, The_Fox, The_Moon):
    def __init__(self, name, strenght, mind, agility, inteligence, spirituality, charisma, luck, current_loc):
        super().__init__(name, strenght, mind, agility, inteligence, spirituality, charisma, luck, current_loc)
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
                   strenght=4,
                   mind=1,
                   agility=7,
                   inteligence=7,
                   spirituality=4,
                   charisma=3,
                   luck=1,
                   current_loc="Mt.Silver"
                   )
haruki = Character(name="Haruki Hirasawa", 
                   strenght=2,
                   mind=1,
                   agility=7,
                   intelect=5,
                   spirituality=7,
                   charisma=3,
                   luck=7,
                   current_loc="The Giant mushroom forest"
                   )
