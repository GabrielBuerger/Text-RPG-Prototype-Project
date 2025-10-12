
class skill():
    def __init__(self, name, user, target, effect):
        self.name = name
        self.user = user
        self.target = target
        self.effect = effect

class physical_skill(skill):
    def __init__(self, name, user, target, effect):
        super().__init__(self, name, user, target, effect)
        pass

class magic_skill(skill):
    def __init__(self, name, user, target, effect):
        super().__init__(self, name, user, target, effect)
        pass

class suport_skill(skill):
    def __init__(self, name, user, target, effect):
        super().__init__(self, name, user, target, effect)
        pass


war_cry = suport_skill("War cry", )
