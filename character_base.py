from random import uniform, randint

class Character:
    def __init__(self, 
                name:str,
                strenght:int,
                mind:int,
                agility:int,
                intelect:int,
                spirituality:int,
                charisma:int,
                luck:int,
                current_loc:str
                ):
#main stats 
        self.name = name
        self.current_loc = current_loc
        self.money = int(0)
        self.inventory = list()
        self.alive = bool(True)
        self.actions = int(1)
        self.passive_skills = list()
        self.physical_skills = list()
        self.magic_skills = list()
        self.suport_skills = list()
#basic stats
        self.strenght = strenght
        self.mind = mind
        self.agility = agility
        self.intelect = intelect
        self.spirit = spirituality
        self.charisma = charisma
        self.luck = luck
#spirituality
        god_blessing = int(self.spirit)^2
#strenght stats
        hp_base = int(25)
        physical_base = int(self.strenght)*2
        #weapon_power = int(1)
        self.max_hp = (int(self.strenght)*hp_base + god_blessing)*10
        self.hp = int(self.max_hp)
        self.physical_damage = physical_base #* weapon_power
        if self.hp == 0:
            self.alive = bool(False)
#mind stats
        self.max_sanity = int(50 + (int(self.mind)*10) + (int(self.luck)))
        self.sanity = int(self.max_sanity)
        self.max_rage = int(50 + (int(self.mind)*6) + (int(self.luck)))
        self.rage = int(0)
#agility stats
        self.armor_wgt_debuff = int(0)
        self.critical = float(int(self.agility) + int(float(self.luck)/2) + int(float(self.intelect)/2))/100
        self.evasion = float(int(self.agility) + (int(self.luck)))/100
        self.run = int(self.agility)
        self.speed = int(self.agility)
#inteligence stats
        mana_base = int(2)
        magic_base = int(self.intelect)*2
        spell_power = int()
        self.magical_damage = magic_base + spell_power
        self.max_mana = (god_blessing + int(self.intelect))*mana_base
        self.mana = int(self.max_mana)
#status:
        self.status = dict()
#basic actions
    def basic_attack(self:'Character', target:'Character'):
        self.physical_damage = int(self.strenght)*2
        crit_bonus = float(2 + (float(self.strenght/10)))
        evasion_chance = float(round(uniform(0,1),2))
        critical_chance = float(round(uniform(0,1),2))
        if float(evasion_chance) <= float(target.evasion):
            self.physical_damage = self.physical_damage*0
            print(f"{target.name} avoided the attack!")
            critical_chance = float(1)
        if float(critical_chance) <= float(self.critical):
            print(f"{self.name} gave critical damage!")
            self.physical_damage = int(self.physical_damage*crit_bonus)
        target.hp -= self.physical_damage
        target.hp = max(target.hp, 0)
    def magic_attack(self:'Character', target:'Character'):
        self.mana -= 8
        self.mana = max(self.mana, 0)
        target.hp -= self.magical_damage
        target.hp = max(target.hp, 0)
    def action(self, target:'Character'):
        while True != 0:
            select = str(randint(1,2))
            if select == "1":
                self.basic_attack(target)
                print(f"{target.name} took {self.physical_damage} damage")
                break
            elif select == "2" and self.mana < 8:
                pass
            elif select == "2":
                self.magic_attack(target)
                print(f"{target.name} took {self.magical_damage} from magical damage")
                print(f"Mana:[{self.max_mana}/{self.mana}]")
                break
    def sanity_check(self):
        if self.sanity < int(float(self.max_sanity)*0.8):
            shadows = list()
            c = 8
            for sanity_left in range(c,0):
                if int(self.sanity) < int(float(self.max_sanity/(float(sanity_left))*10)):
                    c-1
                    shadows.append(Character((f"{self.name}'s Shadow",self,1,1,1,1,1,1,1)))
                    return list(shadows) 
