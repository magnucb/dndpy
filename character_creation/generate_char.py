"""
This is the class where we generate the characters
"""
from domain.lookup import RaceLookup, ProfessionLookup


class CharacterChoice(object):
    def __init__(self):
        self.finished = False
        self.race = None
        self.profession = None

    def select_race(self):
        races = RaceLookup()
        print("Choose your race. Your choices are {}".format(
            races.races))
        self.race = input("Choose a race: ")

    def select_profession(self):
        professions = ProfessionLookup()
        print("Time to to choose a class. Your choices are {}".format(
            professions.professions))
        self.profession = input("Choose a class: ")


def main():
    character = CharacterChoice()
    while not character.finished:
        if not character.race:
            character.select_race()
        if not character.profession:
            character.select_profession()
        else:
            character.finished = True


if __name__ == '__main__':
    main()
