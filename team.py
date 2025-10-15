from player import Player, Character

class Party():
    def __init__(self, members:list[Character]):
        self.members = members
        self.alive = bool(True)
        self.deaths = int(0)
    def show_party(self):
        team_info = dict()
        for member in (0,len(self.members)):
            team_info[str(self.members[member])] = bool(self.members[member].alive)
        if team_info[member].alive == bool(True):
            print(f"{self.members[member]} (ALIVE)", end='')
        elif team_info[str(self.members[member])] == bool(False):
            print(f"{self.members[member]} (DEAD)", end='')
        if member != len(self.members):
            print(", ", end='')
        else:
            print(". ")
    def is_alive(self):
        for member in (0,len(self.members)):
            if self.members[member].alive == False:
                self.deaths += 1
            if self.deaths == len(self.members):
                self.deaths = int(0)
                self.alive = False
            else:
                pass    


class Player_party():
    def __init__(self, protagonist:Player):
        self.protag = protagonist
        self.party_size = int(self.protag.charisma)
        self.members = list()
        self.members.append(self.protag)
        self.deaths = int(0)
        self.alive = bool(True)
    def show_party(self):
        party_info = dict()
        print("Party", end=": ")
        for ally in (0,len(self.members)):
            party_info[str(self.members[ally])] = bool(self.members[ally].alive)
            if party_info[str(self.members[ally])] == bool(True):
                print(f"{self.members[ally].name} (ALIVE)", end='')
            elif party_info[str(self.members[ally])] == bool(False):
                print(f"{self.members[ally].name} (DEAD)", end='')
            if ally != len(self.members):
                print(", ", end='')
            else:
                print(". ")
    def is_alive(self):
        for ally in (0,len(self.members)):
            if self.members[ally].alive == False:
                self.deaths += 1
            if self.deaths == len(self.members):
                self.deaths = int(0)
                self.alive = False
            else:
                pass
    def add_member(self, member:Player):
        self.members.append(member)
