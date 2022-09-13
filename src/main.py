import os
import re
from src.cols import Cols
from data.constants import getConstant
import sys
from src.Num import Num
from src.sym import Sym
from src.data import Data
from src.utils import coerce


# Todo : Move methods into their respective files

'''
Class Csv handles all the utility functions at present
'''


class Csv:
    def __init__(self):
        """
        Constructor to assing initial values
        """
        self.help = getConstant('help')
        tempThe = self.getValuesFromHelp()
        self.the = self.cli(tempThe)
        self.fails = 0

    def getValuesFromHelp(self) -> dict:
        """
        Pull help from constants and parse values into 'the'
        """
        matchedVals = re.findall('\n [-][^\s]+[\s]+[-][-]([^\s]+)[^\n]+= ([^\s]+)', self.help)
        updatedThe = {}
        for val in matchedVals:
            updatedThe[val[0]] = coerce(val[1])
        return updatedThe

    def cli(self, t: dict) -> dict:
        """
        Update value in 'the' based on command line arguments. Print 'help' string if user enters help options
        @t: 'the' object
        """
        tKeys = list(t.keys())
        args = sys.argv
        found = False
        for key in tKeys:
            val = str(t[key])
            for i in range(1, len(args)):
                if args[i] == '-' + key[0:1] or args[i] == '--' + key:
                    found = True
                    val = val == "False" and "True" or val == "True" and "False" or args[i + 1]
            t[key] = coerce(val)
        if t['help'] == True or found == False:
            print('\nIncorrect flag entered. Refer the help string below for correct usage details:') if found == False else None
            print('\n', self.help, '\n')
            exit()
        return t

    def o(self, t: int | float | bool | str | dict) -> str:
        """
        Print values for a column/list or dict
        @t: input to be printed
        """
        if type(t) != dict and type(t) != list:
            return str(t)

        def show(k, v):
            """
            Ignore the values for keys starting with '_', else format the output in the form ':key val' or 'val'
            @k: key
            @v: val
            """
            if str(k).find('_') != 0:
                v = self.o(v)
                return type(t) == dict and ':' + str(k).lower() + ' ' + str(coerce(v)) or str(v)
        valArr = []
        if type(t) == dict:
            for key in list(t.keys()):
                showOutput = show(key, t[key])
                if (showOutput):
                    valArr.append(showOutput)
                valArr.sort()
        elif type(t) == list:
            valArr = t
        return '{' + ' '.join(str(val) for val in valArr) + '}'

    def oo(self, t: dict) -> dict:
        """
        Prints input object
        @t: input object
        """
        print(self.o(t))
        return t

    def rogues(self, b4: dict) -> None:
        """
        Find rogue locals
        @b4: Dictionary of environment variables at the beginning of the run
        """
        envs = dict(os.environ)
        for key in list(envs.keys()):
            if not b4[key]:
                print('?', key, type(envs[key]))

    def csvTestFun(self, rowObj: dict):
        """
        Test function for csv test
        @rowObj: A single row object from the CSV file
        """
        if list(rowObj.keys())[0] > 10:
            return
        else:
            self.oo(list(rowObj.values())[0])

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
            for key in list(self.the.keys()):
                old[key] = self.the[key]
            if self.the['dump'] == True:
                status = True
                out = eg[k]()
            else:
                status = False
                try:
                    out = eg[k]()
                    status = True
                except Exception as e:
                    err = e
                    self.fails += 1
                    # print('Something went wrong. ', e)
            for key in list(old.keys()):
                self.the[key] = old[key]
            msg = status and ((out == True and 'PASS') or 'FAIL') or 'CRASH'
            print('!!!!!!', msg, k, status)
            return out or err

        def Bad():
            """
            Test for a non-existent key
            """
            print(eg['abc'])

        def List():
            """
            Test to sort the list of tests
            """
            t = []
            for i in list(eg.keys()):
                t.append(i)
            t.sort()
            return t

        def Ls():
            """
            Test to print the list of tests
            """
            print('\nExamples python -m src.main -e ...')
            for fun in List():
                print('\t{}'.format(fun))
            return True

        def All():
            """
            Test to run all tests
            """
            for i in List():
                if i != 'ALL':
                    print('\n-----------------------------------')
                    if runs(i) == False:
                        self.fails += 1
            return True

        def the():
            """
            Test to print value in 'the' object
            """
            self.oo(self.the)
            return True

        def sym():
            """
            Test for Sym class
            """
            sym = Sym()
            for x in ["a", "a", "a", "a", "b", "b", "c"]:
                sym.add(x)
            mode, entropy = sym.mid(), sym.div()
            entropy = (1000*entropy)//1/1000
            self.oo({"mid": mode, "div": entropy})
            return mode == "a" and 1.37 <= entropy and entropy <= 1.38

        def num():
            """
            Test for Num class
            """
            num = Num(self.the)
            for i in range(1, 101):
                num.add(i)
            mid, div = num.mid(), num.div()
            print(mid, div)
            return 50 <= mid and mid <= 52 and 30.5 < div and div < 32

        def bignum():
            """
            Test for Num class with reservoir sampler
            """
            num = Num(self.the)
            self.the['nums'] = 32
            for i in range(1, 1001):
                num.add(i)
            self.oo(num.nums())
            return 32 == len(num._has)

        def csv():
            """
            Test for readability from CSV file
            """
            data = Data(self.the, [])
            data.readFromCSV('../data/input.csv', self.csvTestFun)
            return True

        def data():
            """
            Test data class
            """
            data = Data(self.the, '../data/input.csv')
            for col in data.cols.y:
                self.oo(vars(col))
            return True

        def stats():
            """
            Test stats class
            """
            data = Data(self.the, '../data/input.csv')
            def div(col):
                return col.div()
            def mid(col):
                return col.mid()
            print("xmid", self.o( data.stats(2,data.cols.x, mid)))
            print("xdiv", self.o( data.stats(3,data.cols.x, div)))
            print("ymid", self.o( data.stats(2,data.cols.y, mid)))
            print("ydiv", self.o( data.stats(3,data.cols.y, div)))
            return True

        eg = {
            'BAD': Bad,
            'LIST': List,
            'LS': Ls,
            'ALL': All,
            'the': the,
            'sym': sym,
            'num': num,
            'bignum': bignum,
            'csv': csv,
            'data': data,
            'stats': stats
        }
        runs(self.the['eg'])
        return self.fails


def main():
    """
    Main function
    """
    # Find and store environment variables
    b4 = {}
    envs = dict(os.environ)
    for key in list(envs.keys()):
        b4[key] = envs[key]
    # Initiate the main object
    csvObj = Csv()
    fails = csvObj.runTests()
    csvObj.rogues(b4)
    print('\nNumber of failed tests: ', fails)


if __name__ == "__main__":
    main()
