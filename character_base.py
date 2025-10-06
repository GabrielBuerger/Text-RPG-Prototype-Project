from random import randint
from typing import Callable

class Character:
    def __init__(self, 
                name:str,
                strenght:int,
                mind:int,
                agility:int,
                inteligence:int,
                luck:int,
                current_loc:str
                ):
#main stats
        self.name = name
        self.current_loc = current_loc
        self.money = int(0)
        self.alive = bool(True)
        self.actions = int()
        self.attack_moves = list()
        self.status_moves = list()
#basic stats
        self.strenght = strenght
        self.mind = mind
        self.agility = agility
        self.inteligence = inteligence
        self.luck = luck
#strenght stats
        self.max_hp = int(10 + int(self.strenght)*10)
        self.current_hp = int(self.max_hp)
        self.damage = int(2+int(self.strenght))
        if self.current_hp == 0:
            self.alive = bool(False)
#mind stats
        self.max_lunacy = int(self.mind)*6
        self.lunacy = int(self.max_lunacy)
        self.lunacy_resist = int(self.mind)*2
#agility stats
        self.critical = int(self.agility)*2
        self.dodge = int(self.agility)*2
#inteligence stats
        self.magical_damage = int(self.inteligence)
        self.max_mana = int(self.inteligence)*5
        self.mana = int(self.max_mana)
#status:
        self.status = dict()
        self.status = {
            'bleed':0,
            'frozen':0
        }
    def set_status(self, effect:str, duration:int, round:bool=True):
        self.status = dict()
        self.status[effect] = duration
    def round_status(self):
        if self.status['bleed'] > 0:
            bleeding = int(float(self.max_hp)/50)
            self.current_hp -= bleeding
            print(f'{self.name} loses {bleeding}HP by bleeding for {self.status['bleed']} rounds.')
            self.status['bleed'] -= 1
    def turn_satus(self):
        if self.status['frozen'] > 0:
            self.actions = 0
#basic actions
    def basic_attack(self:'Character', target:'Character'):
        self.damage = int(self.strenght)
        dodge = int(randint(0,100))
        critical = int(randint(0,100))
        if dodge <= self.dodge:
            self.damage = self.damage*0
            print(f"{target.name} avoided the attack!")
            critical = 100
        if critical <= self.critical:
            print(f"{self.name} gave critical damage!")
            self.damage = self.damage*2       
        target.current_hp -= self.damage
        target.current_hp = max(target.current_hp, 0)
    def magic_attack(self:'Character', target:'Character'):
        self.mana -= 8
        self.mana = max(self.mana, 0)
        target.current_hp -= self.magical_damage
        target.current_hp = max(target.current_hp, 0)
    def action(self:'Character', target:'Character'):
        print("""
>1 Basic attack
>2 Defend
>3 Atack skills
>4 special skills""")
        select = input("\n>")
        if select == "1":
            self.basic_attack(target)
            print(f"{target.name} taked {self.damage} damage")
        elif select == "2" and self.mana < 8:
            print("You've run out of mana, you can't perform a magical attack")
        elif select == "2":
            self.magic_attack(target)
            print(f"{target.name} taked {self.magical_damage} from magical damage")
            print(f"Mana:[{self.max_mana}/{self.mana}]")
        else:
            print("Invalid input. Please, insert again.")
    # def equip(self, equipment):
