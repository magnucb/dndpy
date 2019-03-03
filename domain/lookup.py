from domain import (race, profession, spell, feature, background, equipment,
                    items)


class RaceLookup(object):
    def __init__(self):
        self.parameters = {
            "dwarf": race.Dwarf,
            "human": race.Human,
        }

    def get(self, item):
        return self.parameters[item]

    def __str__(self):
        return 'race'


class ProfessionLookup(object):
    def __init__(self):
        self.parameters = {
            "paladin": profession.Paladin,
            "ranger": profession.Ranger,
            "bard": profession.Bard,
        }

    def get(self, item):
        return self.parameters[item]

    def __str__(self):
        return 'profession'


class SpellLookup(object):
    def __init__(self):
        self.parameters = {
            "placeholder": spell.Placeholder,
        }

    def get(self, item):
        return self.parameters[item]

    def __str__(self):
        return 'spell'


class FeatureLookup(object):
    def __init__(self):
        self.parameters = {
            "placeholder": feature.Placeholder,
        }

    def get(self, item):
        return self.parameters[item]


class BackgroundLookup(object):
    def __init__(self):
        self.parameters = {
            "charlatan": background.Charlatan,
        }

    def __str__(self):
        return 'background'


class EquipmentLookup(object):
    def __init__(self):
        self.parameters = {
            "placeholder": equipment.Placeholder,
        }

    def __str__(self):
        return 'equipment'


class ItemLookup(object):
    def __init__(self):
        self.parameters = {
            "placeholder": items.Placeholder,
        }

    def __str__(self):
        return 'items'
