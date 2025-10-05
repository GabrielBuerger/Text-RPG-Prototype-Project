from character_base import Character
from battle import *

class Status():
    def __init__(self, effect, duration):
        self.effect = effect
        self.duration = duration
    def set_status(self, effect, duration:int, target:Character):
        self.status.append(effect)
        print(f'{target.name} is now affected by {effect} for {duration} turns.')
    def expire_status():
        pass
    def times(self, target:Character):
        
        self.duration -= 1
        if self.duration == 0:
            pass
            
class Bleed(Status):
    def __init__(self, effect, duration, damage):
        super().__init__(effect, duration)
        self.damage = damage
    def set_status(self, effect, duration, target):
        super().set_status(effect, duration, target)
        bleeding = int(float(target.max_hp)/50)
        target.current_hp -= bleeding
