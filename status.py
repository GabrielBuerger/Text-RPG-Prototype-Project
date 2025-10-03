from character_base import Character

def bleed(target:Character):
        bleeding = int(float(target.max_hp)/50) # /50 = 2%max_hp
        target.current_hp -= bleeding
        print(f'{target} loses {bleeding}HP by bleeding')
