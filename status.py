from character_base import Character

def tbe_list(effect:str, target:Character): #turn_based_effects list
    if target.status[effect] == 'bleed' and target.status[effect] > 0:
        bleeding = int(float(target.max_hp)*(0.02))
        target.hp -= bleeding
        print(f'{target.name} loses {bleeding}HP by bleeding for {target.status['bleed']} rounds.')
        target.status['bleed'] -= 1
    else:
        pass
def rbe_list(effect, target:Character): #round_based_effects list
    if target.status[effect] == 'frozen' and target.status[effect] > 0:
        target.actions = 0
    else:
        pass

def check_type(effect:str, target:Character, type:str):
    if type == "tbe":
        tbe_list(effect, target)
    elif type == "rbe":
        rbe_list(effect, target)
    else:
        tbe_list(effect, target)

class status():
    def __init__(self):
        pass
    def set_status(target:Character, effect:str, duration:int):
        target.status = dict()
        target.status[effect] = duration
    def process_status(target:Character, status_type:str="tbe"):
        for effect in target.status:
            check_type(effect, target, status_type)
