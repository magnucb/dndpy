"""
This is the class where we generate the characters
"""
from domain import lookup
from domain.char import Character


class CharacterChoice(object):
    """Start a character

     Start a character and choose everything to get started playing a level 1
     character.
     """
    def __init__(self):
        self.finished = False
        self.character = Character()

    def select_race(self):
        races = lookup.RaceLookup()
        print("Choose your race. Your choices are {}".format(
            races.races))
        self.character.set_race(input("Choose a race: "))

    def select_profession(self):
        professions = lookup.ProfessionLookup()
        print("Time to to choose a class. Your choices are {}".format(
            professions.professions))
        self.character.set_profession(input("Choose a class: "))

    def select_spell(self):
        spells = lookup.SpellLookup()
        print("Choose spells. Your choices are {}".format(spells.spells))
        choice = input("Choose a spell: ")
        self.character.add_spell(spells.spells.get(choice))

    def select_feature(self):
        features = lookup.FeatureLookup()
        print("Chooce features. Your choices are {}".format(features.features))
        choice = input("Choose a feature: ")
        self.character.add_feature(features.features.get(choice))


def main():
    CharacterChoice()


if __name__ == '__main__':
    main()
