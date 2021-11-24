from abc import abstractmethod, ABCMeta


class IReader(object):
    """Reads json files"""

    @abstractmethod
    def read(self):
        """Reads a file with a default name(The default name is in the initialization of the class)"""

    @abstractmethod
    def read_filename(self, filename):
        """Reads a file with specific name
        filename - the name of the file that the function will open"""
