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
            for stat in stats:
                if stat in self.stats:
                    self.stats[stat] = stats[stat]
        # Check if anything is not set and ask user for input
        # TODO: Make this loop through self.stats and pick which ones to ask
        #  for instead of these ugly if tests.
        if not stats.get('race'):
            self.select_general(lookup.RaceLookup())
        if not stats.get('profession'):
            self.select_general(lookup.ProfessionLookup())
        if not stats.get('spells'):
            self.select_general(lookup.SpellLookup())
        if not stats.get('features'):
            self.select_general(lookup.FeatureLookup())
        if not stats.get('background'):
            self.select_general(lookup.BackgroundLookup())
        if not stats.get('equipment'):
            self.select_general(lookup.EquipmentLookup())
        if not stats.get('items'):
            self.select_general(lookup.ItemLookup())

    def select_general(self, lookup_class):
        print("Choose your {}. Your choices are {}".format(
            lookup_class,
            ', '.join([key for key in lookup_class.parameters.keys()])))
        choice = input("Choose {}: ".format(lookup_class))
        if choice not in lookup_class.parameters:
            print('Unknown {}'.format(lookup_class))
        else:
            self.stats[str(lookup_class)] = choice
        self.stats[str(lookup_class)] = choice


def main():
    character = CharacterChoice(stats={
        'race': 'wrongname',
        'profession': 'bard',
        'spells': 'placeholder',
        'features': 'placeholder',
        'background': 'charlatan',
        "equipment": 'placeholder',
        "items": 'placeholder',
    })
    # Check if any stats are not set and raise an exception if that's the case
    # TODO: We now raise an exception if a character does not have something
    #  of every stat. It may be okay that a character does not have any spells.
    # TODO: Decide if we want to let the users insert unknown names of
    #  things, or we want to implement a check. At the moment anything the
    #  CharacterChoice class gets in the stats parameter is accepted.
    for stat in character.stats:
        if character.stats[stat] is None:
            raise Exception('Missing {} in character.'.format(stat))
    file = datafile.DataFile('testchar.json')
    file.write_file(character.stats)


if __name__ == '__main__':
    main()
