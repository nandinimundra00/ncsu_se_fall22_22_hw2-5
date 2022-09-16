from tst.test_list import TestList


class TestAll:
    """
    Test class for all
    """

    def all(self, misc, eg, runs, fails):
        """
        Test to run all tests
        """
        for i in TestList().list(misc, eg, runs, fails):
            if i != 'ALL':
                print('\n-----------------------------------')
                if runs(i) == False:
                    fails += 1
        return True
