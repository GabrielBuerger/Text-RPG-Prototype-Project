import random

class Character:
    def __init__(self, 
                name:str,
                strenght:int,
                mind:int,
                agility:int,
                inteligence:int,
                luck:int,
                spirit:int,
                ) -> None:
        #main setups
        self.name = name
        self.money = int(0)
        self.alive = bool(True)
        self.status = bool(True)
        #basic stats
        self.strenght = strenght
        self.mind = mind
        self.agility = agility
        self.inteligence = inteligence
        self.luck = luck
        self.spirit = spirit
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

class NPC(Character):
    def __init__(self, name, strenght, mind, agility, inteligence, luck, spirit):
        super().__init__(name, strenght, mind, agility, inteligence, luck, spirit)
    def action(self,target):
        while True:
            select = str(random.randint(1,2))
            if select == "1":
                self.physical_attack(target)
                print(f"{target.name} taked {self.damage} damage")
                break
            elif select == "2" and self.mana < 8:
                pass
            elif select == "2":
                self.magic_attack(target)
                print(f"{target.name} taked {self.magic_damage} from magical damage")
                print(f"Mana:[{self.max_mana}/{self.mana}]")
                break

class Player(Character):
        def __init__(self, name, strenght, mind, agility, inteligence, luck, spirit):
            super().__init__(name, strenght, mind, agility, inteligence, luck, spirit)
            # self.current_loc = current_loc
        # def move(self, current_location, direction):
        #     print(str(map[current_location][direction]))
        #     new_location = str(map[current_location][direction])
        #     print(new_location)
        #     self.current_loc = new_location
        def action(self, target=None):
            while True:
                select = input(">")
                if select == "1":
                    self.physical_attack(target)
                    print(f"{target.name} taked {self.damage} damage")
                    break
                elif select == "2" and self.mana < 8:
                    print("You've run out of mana, you can't perform a magical attack")
                elif select == "2":
                    self.magic_attack(target)
                    print(f"{target.name} taked {self.magic_damage} from magical damage")
                    print(f"Mana:[{self.max_mana}/{self.mana}]")
                    break
                else:
                    print("Invalid input. Please, insert again.")
