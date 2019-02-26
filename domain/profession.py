"""
This is the file where we define all the classes.
Use Profession in the backend to avoid all the horrible things with using a
variable name that is a keyword in python.
"""


class Profession(object):
    def __init__(self):
        pass


class Ranger(Profession):
    def __init__(self):
        super(Ranger, self).__init__()


class Paladin(Profession):
    def __init__(self):
        super(Paladin, self).__init__()
