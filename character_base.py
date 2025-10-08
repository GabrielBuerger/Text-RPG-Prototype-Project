from random import uniform

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
        self.actions = int()
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
        self.critical = int(self.agility)*2
        self.evasion = int(self.agility)*2
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
        dodge = int(uniform(0,1))
        critical = int(uniform(0,1))
        crit_bonus = int(2+(float(self.strenght/10)))
        if dodge <= self.evasion:
            self.damage = self.damage*0
            print(f"{target.name} avoided the attack!")
            critical = 100
        if critical <= self.critical:
            print(f"{self.name} gave critical damage!")
            self.damage = self.damage*crit_bonus
        target.hp -= self.damage
        target.hp = max(target.hp, 0)
    def magic_attack(self:'Character', target:'Character'):
        self.mana -= 8
        self.mana = max(self.mana, 0)
        target.hp -= self.magical_damage
        target.hp = max(target.hp, 0)
    def action(self:'Character', target:'Character'):
        print("""
>1 Basic attack
>2 Defend
>3 Attack skills
>4 special skills""")
        select = input("\n>")
        if select == "1":
            self.basic_attack(target)
            print(f"{target.name} taked {self.damage} damage")
        elif select == "2" and self.mana < 8:
            print("You've run out of mana, you can't perform magic.")
        elif select == "2":
            self.magic_attack(target)
            print(f"{target.name} taked {self.magical_damage} from magical damage")
            print(f"Mana:[{self.max_mana}/{self.mana}]")
        else:
            print("Invalid input. Please, insert again.")
    # def equip(self, equipment):
