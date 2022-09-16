from src.Num import Num


class TestBigNum:
    """
    Test class for bignum
    """

    def bignum(self, misc, eg, runs, fails):
        """
        Test for Num class with reservoir sampler
        """
        num = Num(misc.the)
        misc.the['nums'] = 32
        for i in range(1, 1001):
            num.add(i)
        misc.oo(num.nums())
        return 32 == len(num._has)
