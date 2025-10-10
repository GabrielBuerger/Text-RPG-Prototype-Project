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
        self.alive = bool(True)
        self.actions = int(1)
        self.passive_moves = list()
        self.secret_passive= list()
        self.physical_moves = list()
        self.magic_moves = list()
        self.status_moves = list()
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
        weapon_power = int()
        self.max_hp = (int(self.strenght)*hp_base + god_blessing)*10
        self.hp = int(self.max_hp)
        self.damage = physical_base + weapon_power
        if self.hp == 0:
            self.alive = bool(False)
#mind stats
        self.max_lunacy = int(self.mind)*6
        self.lunacy = int(self.max_lunacy)
        self.lunacy_resist = int(self.mind)*2
        self.max_rage = int(self.mind)*10
        self.rage = int(0)
#agility stats
        self.armor_wgt_debuff = int(0)
        self.critical = float(int(self.agility) + int(float(self.luck)/2) + int(float(self.intelect)/2))/100
        self.evasion = float(int(self.agility) + int(self.luck))/100
        self.speed = int(self.agility)
#inteligence stats
        mana_base = int(2)
        magic_base = int(self.intelect)*2
        spell_power = int()
        self.magical_damage = magic_base + spell_power
        self.max_mana = (god_blessing + int(self.intelect))*mana_base
        self.mana = int(self.max_mana)
#status:
        self.status = {
            'bleed':0,
            'frozen':0
        }
#basic actions
    def basic_attack(self:'Character', target:'Character'):
        self.damage = int(self.strenght)
        crit_bonus = int(2+(float(self.strenght/10)))
        chance = float(uniform(0,1))
        print(chance, target.evasion)
        if chance < target.evasion:
            self.damage = self.damage*0
            print(f"{target.name} avoided the attack!")
        chance = float(uniform(0,1))
        print(chance, target.critical)
        if chance < self.critical:
            print(f"{self.name} gave critical damage!")
            self.damage = self.damage*crit_bonus
        target.hp -= self.damage
        target.hp = max(target.hp, 0)
    def magic_attack(self:'Character', target:'Character'):
        self.mana -= 8
        self.mana = max(self.mana, 0)
        target.hp -= self.magical_damage
        target.hp = max(target.hp, 0)
    def action(self, target:'Character'=None):
        while True != 0:
            select = str(randint(1,2))
            if select == "1":
                self.basic_attack(target)
                print(f"{target.name} taked {self.damage} damage")
                break
            elif select == "2" and self.mana < 8:
                pass
            elif select == "2":
                self.magic_attack(target)
                print(f"{target.name} taked {self.magical_damage} from magical damage")
                print(f"Mana:[{self.max_mana}/{self.mana}]")
                break

