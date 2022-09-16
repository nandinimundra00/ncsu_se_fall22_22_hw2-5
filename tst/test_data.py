from src.data import Data


class TestData:
    """
    Test class for data
    """

    def data(self, misc, eg, runs, fails):
        """
        Test data class
        """
        data = Data(misc, '../data/input.csv')
        for col in data.cols.y:
            misc.oo(vars(col))
        return True
