"""
This is the file where we define all the classes.
Use Profession in the backend to avoid all the horrible things with using a
variable name that is a keyword in python.
"""


class Profession(object):
    def __init__(self):
        self.hitdice = {}

    def levelup(self):
        pass


class Ranger(Profession):
    def __init__(self):
        super(Ranger, self).__init__()


class Paladin(Profession):
    def __init__(self):
        super(Paladin, self).__init__()


class Bard(Profession):
    def __init__(self):
        super(Bard, self).__init__()
        self.hitdice['d8'] = self.hitdice.get('d8', 0) + 1
        self.hitpoints = 8  # TODO: + your constitution modifier
        self.proficiencies = {
            "armor": 'light',
            "weapons": ('simple weapons', 'hand crossbows', 'longswords',
                        'rapiers', 'shortswords', ),
            "tools": '',  # TODO: Choose three instruments of your choice
            "saving throws": ('dex', 'cha', ),
            "skills": '',  # TODO: Choose any three
        }
        # TODO: Make this be in addition to the equipment from background.
        # TODO: Make it possible to choose between the options here
        self.equipment = {
            'rapier',
            'diplomatspack',
            'lute',
            'leatherarmor',
            'dagger',
        }

    def levelup(self):
        super(Bard, self).levelup()
        # TODO: Implement dice roll of 1d8 instead of the flat 5.
        self.hitpoints += 5  # TODO: + your con mod per bard lvl after 1st
