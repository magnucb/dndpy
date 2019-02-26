"""
This file holds classes for handling DnD-datafiles.
"""


class DataFile(object):
    """
    Instance of this class opens a file, reads content as single string,
    and closes file.
    Sorting content-string into useful data is left to other classes.
    """
    def __init__(self, filename):
        self.filename = filename
        self.content = self.read_file()

    def read_file(self):
        """Return data from self.filename as string"""
        with open(self.filename, 'r') as infile:
            content_string = infile.read()
        return str(content_string)

    def write_file(self):
        """Rewrite self.content to self.filename"""
        with open(self.filename, 'w') as outfile:
            outfile.write(self.content)
