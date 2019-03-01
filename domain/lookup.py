from domain import race, profession, spell, feature


class RaceLookup(object):
    def __init__(self):
        self.races = {
            "dwarf": race.Dwarf,
            "human": race.Human,
        }

    def get(self, item):
        return self.races[item]


class ProfessionLookup(object):
    def __init__(self):
        self.professions = {
            "paladin": profession.Paladin,
            "ranger": profession.Ranger,
        }

    def get(self, item):
        return self.professions[item]


class SpellLookup(object):
    def __init__(self):
        self.spells = {
            "placeholder": spell.Placeholder,
        }

    def get(self, item):
        return self.spells[item]


class FeatureLookup(object):
    def __init__(self):
        self.features = {
            "placeholder": feature.Placeholder,
        }

    def get(self, item):
        return self.features[item]
