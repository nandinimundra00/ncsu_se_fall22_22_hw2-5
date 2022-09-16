from tst.test_list import TestList


class TestLs:
    """
    Test class for ls
    """

    def ls(self, misc, eg, runs, fails):
        """
        Test to print the list of tests
        """
        print('\nExamples python -m src.main -e ...')
        for fun in TestList().list(misc, eg, runs, fails):
            print('\t{}'.format(fun))
        return True
