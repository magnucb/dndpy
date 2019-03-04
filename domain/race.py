"""
This is the class where all the races are defined.
"""


class Race(object):
    def __init__(self):
        self.abilityscores = {
            "str": 11,
            "dex": 11,
            "con": 11,
            "int": 11,
            "wis": 11,
            "cha": 11,
        }
        self.size = ''
        self.speed = 0
        self.hitpointmax = 10

    def levelup(self):
        pass


class Human(Race):
    def __init__(self):
        super(Human, self).__init__()

    def levelup(self):
        super(Human, self).levelup()

    def __str__(self):
        return 'Human'


class Dwarf(Race):
    def __init__(self):
        super(Dwarf, self).__init__()
        self.abilityscores["con"] += 1
        self.size = 'medium'
        self.speed = 25

    def levelup(self):
        super(Dwarf, self).levelup()

    def __str__(self):
        return 'Dwarf'


class HillDwarf(Dwarf):
    def __init__(self):
        super(HillDwarf, self).__init__()
        self.abilityscores["wis"] += 1
        self.hitpointmax += 1

    def levelup(self):
        self.hitpointmax += 1

    def __str__(self):
        return 'HillDwarf'


class MountainDwarf(Dwarf):
    def __init__(self):
        super(MountainDwarf, self).__init__()
        self.abilityscores["str"] += 2
        self.hitpointmax += 1
        # TODO: Add proficiency with light and medium armor

    def levelup(self):
        self.hitpointmax += 1

    def __str__(self):
        return 'MountainDwarf'
