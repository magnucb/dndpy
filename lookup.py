import race
import profession


def select_race(choice):
    """

    :param choice:
    :return:
    """
    races = {
        "dwarf": race.Dwarf,
        "human": race.Human,
    }
    return races[choice]()


def select_profession(choice):
    """

    :param choice:
    :return:
    """
    professions = {
        "Paladin": profession.Paladin,
        "Ranger": profession.Ranger,
    }
    return professions[choice]()
