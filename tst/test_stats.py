from src.data import Data


class TestStats:
    """
    Test class for stats
    """

    def stats(self, misc, eg, runs, fails):
        """
        Test stats class
        """
        data = Data(misc, '../data/input.csv')

        def div(col):
            return col.div()

        def mid(col):
            return col.mid()
        print("xmid", misc.o(data.stats(2, data.cols.x, mid)))
        print("xdiv", misc.o(data.stats(3, data.cols.x, div)))
        print("ymid", misc.o(data.stats(2, data.cols.y, mid)))
        print("ydiv", misc.o(data.stats(3, data.cols.y, div)))
        return True
