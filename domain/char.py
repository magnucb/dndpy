class Character(object):
    """

    """
    def __init__(self):
        """

        """
        self._race = None
        self._profession = None
        self._background = None
        self._alive = True
        self.level = 1
        self.equipment = {

        }
        self.features = {

        }
        self.spells = {

        }
        self.items = {

        }

    # Kill/Resurrect
    def kill(self):
        self._alive = False

    def resurrect(self):
        self._alive = True

    # Race
    def get_race(self):
        return self._race

    def set_race(self, race):
        self._race = race

    # Profession(Class)
    def get_profession(self):
        return self._profession

    def set_profession(self, profession):
        self._profession = profession

    # Background
    def get_background(self):
        return self._background

    def set_background(self, background):
        self._background = background

    # Equipment
    def get_equipment(self):
        return self.equipment

    def del_equipment(self):
        self.equipment = {}

    def add_equipment(self, equipment):
        self.equipment.update(equipment)

    # Level up and down
    def level_up(self, level):
        self.level += level

    def level_down(self, level):
        self.level -= level

    # Features
    def get_features(self):
        return self.features

    def add_feature(self, feature):
        self.features.update(feature)

    # Spells
    def get_spells(self):
        return self.spells

    def add_spell(self, spell):
        self.spells.update(spell)

    def del_spell(self, item):
        try:
            del self.spells[item]
        except KeyError:
            return False
        else:
            return True

    # Items
    def get_items(self):
        return self.items

    def add_item(self, item):
        self.items.update(item)

    def del_item(self, item):
        try:
            del self.items[item]
        except KeyError:
            return False
        else:
            return True
