"""
This is the class where we generate the characters
"""


class makechar(object):

    def allocate_baseattributes(self, racechoice, level, background):
        available_choices = {
            "dwarf": Dwarf,
            "human": Human
        }

