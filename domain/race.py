"""
This is the class where all the races are defined.
"""


class Race(object):
    def __init__(self):
        self.stats = {
            "str": 11,
            "dex": 11,
        }

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

    def levelup(self):
        super(Dwarf, self).levelup()

    def __str__(self):
        return 'Dwarf'
