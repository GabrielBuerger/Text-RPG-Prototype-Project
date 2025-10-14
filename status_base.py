from character_base import Character

class Status():
    def __init__(self):
        pass
    def set_status(target:Character, effect:str, duration:int):
        target.status:dict[str,int] = effect, duration
    def proccess_status(target:Character):
        if not target.status:
            return
        for effect, duration in target.status.items():
            if duration == 0:
                del target.status[effect]
                break
            else:
                status_list(target, effect)
                target.status[effect] -=1

def status_list(target:Character, effect:str):
    if effect == 'bleed':
        bleeding = int(float(target.max_hp)*(0.02))
        target.hp -= bleeding
        print(f'{target.name} loses {bleeding}HP by bleeding for {target.status['bleed']} rounds.')
    elif effect == 'insanity':
        target.sanity -= 10
        print(f"{target.name}'s sanity felt 10pts ({target.sanity}/{target.max_sanity})")
    else:
        return
