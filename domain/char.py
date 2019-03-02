"""
This is the class where we make the character object.
"""


class Character(object):
    def __init__(self, stats):
        self._race = stats['race']
        self._profession = stats['profession']
        self._background = stats['background']
        self._alive = True
        self.level = 1
        self.equipment = stats['equipment']
        self.features = stats['features']
        self.spells = stats['spells']
        self.items = stats['items']

    # Kill/Resurrect
    def kill(self):
        self._alive = False

    def resurrect(self):
        self._alive = True

    # Level up and down
    def level_up(self, level):
        self.level += level

    def level_down(self, level):
        self.level -= level

    # Race
    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, race):
        self._race = race

    @race.deleter
    def race(self):
        self._race = None

    # Profession(Class)
    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, profession):
        self._profession = profession

    # Background
    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, background):
        self._background = background

    # Equipment
    @property
    def equipment(self):
        return self.equipment

    @equipment.setter
    def equipment(self, equipment):
        self.equipment = equipment

    @equipment.deleter
    def equipment(self):
        del self.equipment

    # Features
    @property
    def features(self):
        return self.features

    @features.setter
    def features(self, feature):
        self.features = feature

    @features.deleter
    def features(self):
        del self.features

    # Spells
    @property
    def spells(self):
        return self.spells

    @spells.setter
    def spells(self, spell):
        self.spells = spell

    @spells.deleter
    def spells(self):
        del self.spells

    # Items
    @property
    def items(self):
        return self.items

    @items.setter
    def items(self, item):
        self.items = item

    @items.deleter
    def items(self):
        del self.items
