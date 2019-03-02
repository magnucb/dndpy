"""
This is the class where we generate the characters
"""
from domain import lookup
from data import datafile


class CharacterChoice(object):
    """Start a character

     Start a character and choose everything to get started playing a level 1
     character.
     """
    def __init__(self, stats=None):
        self.finished = False
        self.stats = {
            'race': None,
            'profession': None,
            'background': None,
            'equipment': None,
            'features': None,
            'spells': None,
            'items': None,
        }
        # Accept a start input with known values.
        if stats:
            for stat, val in stats:
                if stat in self.stats:
                    self.stats[stat] = val

    # TODO: These are four identical methods. Make a general selector function.
    def select_race(self):
        races = lookup.RaceLookup()
        print("Choose your race. Your choices are {}".format(
            races.races))
        choice = input("Choose a race: ")
        self.stats['race'] = races.races.get(choice)

    def select_profession(self):
        professions = lookup.ProfessionLookup()
        print("Choose your class. Your choices are {}".format(
            professions.professions))
        choice = input("Choose a class: ")
        self.stats['profession'] = professions.professions.get(choice)

    def select_spell(self):
        spells = lookup.SpellLookup()
        print("Choose spells. Your choices are {}".format(spells.spells))
        choice = input("Choose a spell: ")
        self.stats['spells'] = spells.spells.get(choice)

    def select_feature(self):
        features = lookup.FeatureLookup()
        print("Choose features. Your choices are {}".format(features.features))
        choice = input("Choose a feature: ")
        self.stats['features'] = features.features.get(choice)


def main():
    character = CharacterChoice()
    file = datafile.DataFile('testchar.json')
    file.write_file(character.stats)


if __name__ == '__main__':
    main()
