from random import random

class Character:
    def __init__(self, 
                name:str,
                strenght:int,
                mind:int,
                agility:int,
                inteligence:int,
                luck:int,
                current_loc:str="Void"
                ) -> None:
        #main setups
        self.name = name
        self.current_loc = current_loc
        self.money = int(0)
        self.alive = bool(True)
        self.status = bool(True)
        #basic stats
        self.strenght = strenght
        self.mind = mind
        self.agility = agility
        self.inteligence = inteligence
        self.luck = luck
        #strenght stats
        self.max_hp = int(10 + int(self.strenght)*5)
        self.current_hp = int(self.max_hp)
        self.damage = int(2+int(self.strenght))
        if self.current_hp == 0:
            self.alive = False
        #mind stats
        self.max_lunacy = int(self.mind)*6
        self.lunacy = int(self.max_lunacy)
        self.lunacy_resist = int(self.mind)*2
        #agility stats
        self.critical = int(self.agility)*2
        self.dodge = int(self.agility)*2
        #inteligence stats
        self.magic_damage = int(self.inteligence)
        self.max_mana = int(self.inteligence)*5
        self.mana = int(self.max_mana)
    def physical_attack(self, target:str) -> None:
        self.damage = int(self.strenght)
        dodge = int(random.randint(0,100))
        critical = int(random.randint(0,100))
        if dodge <= self.dodge:
            self.damage = self.damage*0
            print(f"{target.name} avoided the attack!")
            critical = 100
        # print(critical_value, "/", self.critical_chance, "%")
        if critical <= self.critical:
            print(f"{self.name} gave critical damage!")
            self.damage = self.damage*2       
        target.current_hp -= self.damage
        target.current_hp = max(target.current_hp, 0)
    def magic_attack(self, target):
        self.mana -= 8
        self.mana = max(self.mana, 0)
        # dodge = int(random.randint(0,100))
        # if dodge <= self.dodge:
        #     self.damage = self.damage*0
        #     print(f"{target.name} avoided the attack!")
        target.current_hp -= self.magic_damage
        target.current_hp = max(target.current_hp, 0)
    # def equip(self, equipment):
