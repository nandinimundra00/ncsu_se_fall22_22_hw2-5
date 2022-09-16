from tst.test_all import TestAll
from tst.test_bad import TestBad
from tst.test_bignum import TestBigNum
from tst.test_csv import TestCsv
from tst.test_data import TestData
from tst.test_list import TestList
from tst.test_ls import TestLs
from tst.test_num import TestNum
from tst.test_stats import TestStats
from tst.test_sym import TestSym
from tst.test_the import TestThe

"""
Test engine class
"""


class Tests:
    def __init__(self, misc):
        """
        Constructor for test engine
        """
        self.fails = 0
        self.misc = misc

    def runTests(self):
        """
        Runs all defined tests
        """
        def runs(k):
            """
            Runs a specific test
            @k: Key of test
            """
            err = ''
            if k not in eg:
                return
            old = {}
            out = None
            for key in list(self.misc.the.keys()):
                old[key] = self.misc.the[key]
            if self.misc.the['dump'] == True:
                status = True
                out = eg[k](self.misc, eg, runs, self.fails)
            else:
                status = False
                try:
                    out = eg[k](self.misc, eg, runs, self.fails)
                    status = True
                except Exception as e:
                    err = e
                    self.fails += 1
                    # print('Something went wrong. ', e)
            for key in list(old.keys()):
                self.misc.the[key] = old[key]
            msg = status and ((out == True and 'PASS') or 'FAIL') or 'CRASH'
            print('!!!!!!', msg, k, status)
            return out or err

        eg = {
            'BAD': TestBad().bad,
            'LIST': TestList().list,
            'LS': TestLs().ls,
            'ALL': TestAll().all,
            'the': TestThe().the,
            'sym': TestSym().sym,
            'num': TestNum().num,
            'bignum': TestBigNum().bignum,
            'csv': TestCsv(self.misc).csv,
            'data': TestData().data,
            'stats': TestStats().stats
        }
        runs(self.misc.the['eg'])
        return self.fails
