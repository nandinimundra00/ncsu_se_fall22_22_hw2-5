from src.data import Data


class TestCsv:
    """
    Test class for csv
    """

    def __init__(self, misc) -> None:
        """
        Constructor for csv class
        """
        self.misc = misc

    def csvTestFun(self, rowObj: dict):
        """
        Test function for csv test
        @rowObj: A single row object from the CSV file
        """
        if list(rowObj.keys())[0] > 10:
            return
        else:
            self.misc.oo(list(rowObj.values())[0])

    def csv(self, misc, eg, runs, fails):
        """
        Test for readability from CSV file
        """
        data = Data(misc, [])
        data.readFromCSV('../data/input.csv', self.csvTestFun)
        return True
