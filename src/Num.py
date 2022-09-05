import math
import sys
import random

#global variables
the = {'nums': 512}

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

    def __init__(self, c=0, s=""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}
        self.lo = sys.maxsize
        self.hi = -sys.maxsize
        self.isSorted = True
        self.w = 1 if (s or "").find("-$") == -1 else -1

    '''
    Return kept numbers, sorted
    '''

    def nums(self) -> dict:
        if not self.isSorted:
            self._has = dict(sorted(self._has.items()))
            self.isSorted = True
        return self._has

    '''
    Reservoir sampler. Keep at most `the['nums']` numbers 
    (and if we run out of room, delete something old, at random).,
    Arguments:
    @v:
    '''

    def add(self, v):
        global the
        pos = -1
        if v != "?":
            self.n = self.n+1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            if len(self._has) < the['nums']:
                pos = 1+(len(self._has))
            elif random.randint(0, 1) < (the['nums']/self.n):
                pos = random.randint(1, len(self._has))
            if pos:
                self.isSorted = False
                self._has[pos] = v

    def per(self, t, p):
        p = math.floor(((p or 0.5) * len(t)) + 0.5)
        return t[max(1, min(len(t), p))]

    '''
    Diversity (standard deviation for Nums, entropy for Syms)
    '''

    def div(self) -> float:
        a = self.nums()
        # 2.58 as per (https://github.com/txt/se22/blob/main/etc/pdf/csv.pdf). Readme in HW states 2.56 though
        return (self.per(a, 0.9)-self.per(a, 0.1))/2.58

    '''
    Central tendancy (median for Nums, mode for Syms)
    '''

    def mid(self) -> float:
        return self.per(self.nums(), 0.5)


def o(t):
    if type(t) != list:
        return str(t)

    def show(k, v):
        if str(k).find('^_') == -1:
            v = o(v)
            return len(t) == 0 and format(':{} {}', k, v) or str(v)
    valArr = []
    counter = 0
    tKeys = list(t.keys())
    for key in tKeys:
        valArr[counter] = show(key, t[key])
    if len(t) == 0:
        valArr.sort()
    return '{' + ' '.join(str(val) for val in valArr) + '}'


# Testing Num class
def oo(t):
    print(o(t))
    return t
