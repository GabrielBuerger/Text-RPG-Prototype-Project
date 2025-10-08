from player import Player, Character

class Enemy_party():
    def __init__(self, members:list[Character]=None):
        self.members = members
        self.alive = bool(False)
        self.deaths = int(0)
    def show_team(self):
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
    def __init__(self, protagonist:Player, allies:list[Character]|Character=None):
        self.protag = protagonist
        self.allies = allies
        self.party_size = int(self.protag.charisma)
        self.members = list([None] * self.party_size)
        self.members.append(self.protag)
        if isinstance(allies, Character):
            self.members.append(self.allies)
        else:
            for member in range(0, len(list(self.allies))):
                self.members.append(self.allies[member])
        self.deaths = int(0)
        self.alive = bool(True)
    def show_party(self):
        party_info = dict()
        print("Party", end=": ")
        for ally in (0,len(self.members)):
            party_info[str(self.members[ally])] = bool(self.members[ally].alive)
            if party_info[str(self.members[ally])] == bool(True):
                print(f"{self.members[ally]} (ALIVE)", end='')
            elif party_info[str(self.members[ally])] == bool(False):
                print(f"{self.members[ally]} (DEAD)", end='')
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
