from character_base import Character
from player import Player

class Team():
    def __init__(self, character1:Character,
                 character2:Character=None, 
                 character3:Character=None,
                 character4:Character=None):
        self.p1 = character1
        self.p2 = character2
        self.p3 = character3
        self.p4 = character4
        self.alive = bool(False)
        if self.p1.alive == False and self.p2.alive == False and self.p3.alive == False and self.p4.alive == False:
            self.alive = bool(False)

class Party():
    def __init__(self, protagonist:Player, members:list[Player]):
        self.protag = protagonist
        self.members = members
        self.party_size = int(self.protag.charisma)
        self.members = list([None] * self.party_size)
        self.members.insert(0,self.protag)
        self.deaths = int(0)
        self.alive = bool(True)
    def show_party(self):
        party_info = dict()
        print("Party", end=": ")
        for player in (0,len(self.members)):
            party_info[str(self.members[player])] = bool(self.members[player].alive)
            if party_info[str(self.members[player])] == bool(True):
                print(f"{self.members[player]} (ALIVE)")
            elif party_info[str(self.members[player])] == bool(False):
                print(f"{self.members[player]} (DEAD)")
    def is_alive(self):
        for player in (0,len(self.members)):
            if self.members[player].alive == False:
                self.deaths += 1
            if self.deaths == len(self.members):
                self.deaths = int(0)
                self.alive = False
            else:
                pass
