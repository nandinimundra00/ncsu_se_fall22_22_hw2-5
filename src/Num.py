import math
import sys
import random
import re


'''
Class `Num` Summarizes a stream of numbers. 
'''


class Num:
    '''
    Constuctor which initializes the attributes

    Attributes:
    @n: items seen
    @at: column position
    @name: column name
    @_has: kept data
    @lo: lowest seen
    @hi: highest seen
    @isSorted: no updates since last sort of data
    @w: 
    Arguments:
    @c: column postition
    @s: column name
    '''

    def __init__(self, the, c=0, s=""):
        self.n = 0
        self.at = c + 1
        self.name = s
        self._has = {}
        self.lo = sys.maxsize
        self.hi = -sys.maxsize
        self.isSorted = True
        self.w = -1 if re.search("-$", s or '') else 1
        self._the = the
        random.seed(self._the['seed'])

    '''
    Return kept numbers, sorted
    '''

    def nums(self) -> dict:
        vals = list(self._has.values())
        if not self.isSorted:
            vals.sort()
            self.isSorted = True
        return vals

    '''
    Reservoir sampler. Keep at most `the['nums']` numbers 
    (and if we run out of room, delete something old, at random).,
    Arguments:
    @v:
    '''

    def add(self, v):
        floatV = float(v)
        pos = -1
        if floatV != "?":
            self.n = self.n + 1
            self.lo = min(floatV, self.lo)
            self.hi = max(floatV, self.hi)
            if len(self._has) < self._the['nums']:
                pos = 1 + (len(self._has))
            elif random.random() < (self._the['nums']/self.n):
                pos = random.randint(1, len(self._has))
            if pos != -1:
                self.isSorted = False
                self._has[pos] = v

    def per(self, t, p):
        p = math.floor(((p or 0.5) * len(t)) + 0.5)
        return t[max(1, min(len(t), p)) - 1]

    '''
    Diversity (standard deviation for Nums, entropy for Syms)
    '''

    def div(self) -> float:
        a = self.nums()
        # 2.58 as per (https://github.com/txt/se22/blob/main/etc/pdf/csv.pdf). Readme in HW states 2.56 though
        return (self.per(a, 0.9) - self.per(a, 0.1)) / 2.58

    '''
    Central tendancy (median for Nums, mode for Syms)
    '''

    def mid(self) -> float:
        return self.per(self.nums(), 0.5)
