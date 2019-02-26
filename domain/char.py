from domain import lookup


class Character(object):
    """

    """
    def __init__(self, race, profession):
        """

        :param race:
        :param profession:
        """
        self.race = lookup.select_race(race)
        self.profession = lookup.select_profession(profession)
        self.equipment = {

        }
        self.alive = True
