from abc import ABCMeta, abstractmethod


class IWriter:
    """Puts data in json files"""

    @abstractmethod
    def write_filename(self, filename, data):
        """Puts specific data  in json file with specific name
        filename - the name of the file that the function will open
        data - the data that the function will put in file"""