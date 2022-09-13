import os
import csv
import math
from src.Num import Num
from src.sym import Sym
from src.cols import Cols
from src.row import Row
from src.utils import coerce

'''
Class `Data` is a holder of `rows` and their summaries (in `cols`)
'''


class Data:
    '''
    Constuctor which initializes the attributes

    Attributes:
    @cols: column class single object....no list here unlike rows....see next line :)
    @rows: storing Rows class objects

    Arguments:
    @src: input file name
    '''

    def __init__(self, the, src) -> None:
        self.cols = None
        self.rows = []
        self._the = the

        '''
        Check if the recived file name (variable src) is a string. 
        If yes, then run csv function on it and also send add function name 
        If no, we get that someone tried being cheeky here. They gave us a list of rows
        of the file directly and didn't trust us :(
        We simply use the add function directly here instead of asking csv function
        to read each row and then use it.
        '''

        if type(src) == str:
            self.readFromCSV(src, self.add)
        else:
            for i in range(len(src)):
                self.add(src[i])

    def readFromCSV(self, fname: str, funcnm) -> None:
        """
        Read content from CSV file and run a custom function on each row
        @fname: file path with file name
        @funcnm: custom user function
        """
        sep = self._the['Seperator']
        currentWorkingPath = os.path.dirname(__file__)
        relativePath = os.path.join(currentWorkingPath, fname)
        with open(relativePath, 'r') as file:
            reader = csv.reader(file, delimiter=sep)
            n = 0
            for row in reader:
                n = n + 1
                parsedRow = []
                for col in row:
                    parsedRow.append(coerce(col))
                funcnm({n: parsedRow})

    def add(self, xs):
        """
        Add a `row` to `data`. Calls `add()` to  updatie the `cols` with new values.
        @xs: dict with a single key, value pair. The value holds the entire row as a list 
        """
        # Check if cols is none then its the first row and will considered as column headers
        if self.cols is None:
            # pass the list of column headers to create an object of class Cols
            self.cols = Cols(list(xs.values())[0], self._the)
        else:
            # create an object of class Row and append it to our list `rows`
            temp_row = Row(xs)
            self.rows.append(temp_row)
            # todo is a list of dependent and independent columns which are objects of class Num or Sym
            todo = self.cols.x + self.cols.y
            for obj_col in todo:
                obj_col.add(list(temp_row.cells.values())[0][obj_col.at - 1])

    def rnd(self, x, places):
        mult = math.pow(x,places)
        result =  math.floor(x * mult + 0.5) / mult
        return result


    def stats(self, places=None, showcols=None, funcnm=None) -> dict:
        if places is None:
            places = 2
        if showcols is None:
            showcols = self.cols.y
        if funcnm is None:
            funcnm = 'mid'
        t = {}
        print(showcols)
        for i in range(showcols):
            fun = getattr(showcols[i], funcnm)
            v = fun()
            #print(v)
            if type(v) == int:
                v = self.rnd(v, places)
            t[showcols[i].name] = v
        return t


''' Can remove after testing, just to see the values outputted from the variables'''
# def showStats():
#     src = '../data/input.csv'
#     the = {"Seperator":","}
#     data = Data(the, src)

#     cols = data.cols


#     for i in cols.all:
#         print(i.name)

#     print("-"*100)
#     for i in cols.x:
#         print(i.name)
#         print(i._has)
#         print(i.at)
#     # print(cols.x)
#     # print(cols.y)
#     print("-"*100)
#     for i in cols.y:
#         print(i.name)
#     print("-"*100)
#     print(cols.names)
#     print(cols.klass)

#     print(data.stats(func = 'mid'))


# showStats()
