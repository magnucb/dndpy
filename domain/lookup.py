from domain import race, profession


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
