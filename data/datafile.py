"""
This file holds classes for handling DnD-datafiles.
"""
import json


class DataFile(object):
    """
    Instance of this class opens a file, reads content as single string,
    and closes file.
    Sorting content-string into useful data is left to other classes.
    """
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, 'r') as json_file:
            data = json.load(json_file)
        return data

    def write_file(self, content):
        """Write self.content to self.filename"""
        with open(self.filename, 'w') as json_file:
            json.dump(content, json_file)
