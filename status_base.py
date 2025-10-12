from character_base import Character

class Status():
    def __init__(self):
        pass
    def set_status(target:Character, effect:str, duration:int):
        target.status = dict()
        target.status[effect] = duration
    def get_status(target:Character, status_type:bool=True):
        #Turn_based_effect <- (status_type = True)
        #Round_based_effect <- (status_type = False)
        if not target.status:
            return
        else:
            proccess_status(target, status_type)

def proccess_status(target:Character, status_type:bool):
    for effect in target.status:
        if target.status[effect] == 0:
            del target.status[effect]
            break
        if status_type:
            tbe_list(target, effect)
            continue
        else:
            rbe_list(target, effect)

def rbe_list(target:Character, effect:str):
    if effect == "frozen":
        pass
    else:
        return
    target.status[effect] -= 1

def tbe_list(target:Character, effect:str):
    if effect == 'bleed':
        bleeding = int(float(target.max_hp)*(0.02))
        target.hp -= bleeding
        print(f'{target.name} loses {bleeding}HP by bleeding for {target.status['bleed']} rounds.')
    else:
        return
    target.status[effect] -= 1
