class item():
    def __init__(self, name:str, type, stackable:bool):
        self.name = name
        self.type = type
        self.stackable = stackable

#Basic item classes:

class weapon(item):
    def __init__(self, name, type, damage:int, range:int, stackable = False):
        super().__init__(name, type, stackable)
        self.damage = damage
        self.range = range

class armor(item):
    def __init__(self, name, type, defense, stackable = False):
        super().__init__(name, type, stackable)
        self.defense = defense

class consumable(item):
    def __init__(self, name, type, stackable = True):
        super().__init__(name, type, stackable)

class tools(item):
    def __init__(self, name, type, stackable):
        super().__init__(name, type, stackable)

class skill_book(item):
    def __init__(self, name, type, stackable):
        super().__init__(name, type, stackable)

class quest_item(item):
    def __init__(self, name, type, stackable):
        super().__init__(name, type, stackable)

#weapon class:

class mellee(weapon):
    def __init__(self, name, type, damage, range, stackable=False):
        super().__init__(name, type, damage, range, stackable)

class ranged(weapon):
    def __init__(self, name, type, damage, range, stackable=False):
        super().__init__(name, type, damage, range, stackable)
