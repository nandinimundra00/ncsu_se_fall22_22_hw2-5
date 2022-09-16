class TestList:
    """
    Test class for list
    """

    def list(self, misc, eg, runs, fails):
        """
        Test to sort the list of tests
        """
        t = []
        for i in list(eg.keys()):
            t.append(i)
        t.sort()
        return t
