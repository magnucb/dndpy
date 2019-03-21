"""
This is the file where we define all the skills.
"""


class Skill(object):
    def __init__(self):
        pass


class Acrobatics(Skill):
    def __init__(self):
        super(Acrobatics, self).__init__()
        self.ability_link = 'dex'

    def __str__(self):
        return "Acrobatics"

    def description(self):
        pass


class AnimalHandling(Skill):
    def __init__(self):
        super(AnimalHandling, self).__init__()
        self.ability_link = 'wis'

    def __str__(self):
        return "Animal Handling"

    def description(self):
        pass


class Arcana(Skill):
    def __init__(self):
        super(Arcana, self).__init__()
        self.ability_link = 'int'

    def __str__(self):
        return "Arcana"


class Athletics(Skill):
    def __init__(self):
        super(Athletics, self).__init__()
        self.ability_link = 'str'

    def __str__(self):
        return "Athletics"


class Deception(Skill):
    def __init__(self):
        super(Deception, self).__init__()
        self.ability_link = 'cha'

    def __str__(self):
        return "Deception"


class History(Skill):
    def __init__(self):
        super(History, self).__init__()
        self.ability_link = 'int'

    def __str__(self):
        return "History"


class Insight(Skill):
    def __init__(self):
        super(Insight, self).__init__()
        self.ability_link = 'wis'

    def __str__(self):
        return "Insight"


class Intimidation(Skill):
    def __init__(self):
        super(Intimidation, self).__init__()
        self.ability_link = 'cha'

    def __str__(self):
        return "Intimidation"


class Investigation(Skill):
    def __init__(self):
        super(Investigation, self).__init__()
        self.ability_link = 'int'

    def __str__(self):
        return "Investigation"


class Medicine(Skill):
    def __init__(self):
        super(Medicine, self).__init__()
        self.ability_link = 'wis'

    def __str__(self):
        return "Medicine"


class Nature(Skill):
    def __init__(self):
        super(Nature, self).__init__()
        self.ability_link = 'int'

    def __str__(self):
        return "Nature"


class Perception(Skill):
    def __init__(self):
        super(Perception, self).__init__()
        self.ability_link = 'wis'

    def __str__(self):
        return "Perception"


class Performance(Skill):
    def __init__(self):
        super(Performance, self).__init__()
        self.ability_link = 'cha'

    def __str__(self):
        return "Performance"


class Persuasion(Skill):
    def __init__(self):
        super(Persuasion, self).__init__()
        self.ability_link = 'cha'

    def __str__(self):
        return "Persuasion"


class Religion(Skill):
    def __init__(self):
        super(Religion, self).__init__()
        self.ability_link = 'int'

    def __str__(self):
        return "Religion"


class SleightOfHand(Skill):
    def __init__(self):
        super(SleightOfHand, self).__init__()
        self.ability_link = 'dex'

    def __str__(self):
        return "Sleight of Hand"


class Stealth(Skill):
    def __init__(self):
        super(Stealth, self).__init__()
        self.ability_link = 'dex'

    def __str__(self):
        return "Religion"


class Survival(Skill):
    def __init__(self):
        super(Survival, self).__init__()
        self.ability_link = 'wis'

    def __str__(self):
        return "Survival"
