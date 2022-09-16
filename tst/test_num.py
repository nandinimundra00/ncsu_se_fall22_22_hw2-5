from src.Num import Num


class TestNum:
    """
    Test class for num
    """

    def num(self, misc, eg, runs, fails):
        """
        Test for Num class
        """
        num = Num(misc.the)
        for i in range(1, 101):
            num.add(i)
        mid, div = num.mid(), num.div()
        print(mid, div)
        return 50 <= mid and mid <= 52 and 30.5 < div and div < 32
