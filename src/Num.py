import math
import sys
import random
import re


class Num:
    '''
    Class `Num` Summarizes a stream of numbers. 
    '''

    def __init__(self, the, c=0, s=""):
        '''
        Arguments
        ----------
        c : column postition
        s : column name
        '''
        self.n = 0
        '''Items seen'''
        self.at = c + 1
        '''column position'''
        self.name = s
        '''column name'''
        self._has = {}
        '''kept data'''
        self.lo = sys.maxsize
        '''lowest seen'''
        self.hi = -sys.maxsize
        '''highest seen'''
        self.isSorted = True
        '''no updates since last sort'''
        self.w = -1 if re.search("-$", s or '') else 1
        self._the = the
        random.seed(self._the['seed'])


    def nums(self) -> dict:
        '''
        Return kept numbers, sorted
        '''
        vals = list(self._has.values())
        if not self.isSorted:
            vals.sort()
            for i in range(1, len(vals) + 1):
                self._has[i] = vals[i - 1]
            self.isSorted = True
        return vals



    def add(self, v):
        '''
        Reservoir sampler. Keep at most `the['nums']` numbers 
        (and if we run out of room, delete something old, at random).

        Arguments
        ----------
        v : Value to be added
        '''
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
        '''Mathematical formula for getting standard deviation'''
        p = math.floor(((p or 0.5) * len(t)) + 0.5)
        return t[max(1, min(len(t), p)) - 1]


    def div(self) -> float:
        '''
        Diversity (standard deviation for Nums, entropy for Syms)
        '''
        a = self.nums()
        # 2.58 as per (https://github.com/txt/se22/blob/main/etc/pdf/csv.pdf). Readme in HW states 2.56 though
        return round((self.per(a, 0.9) - self.per(a, 0.1)) / 2.58, 3)


    def mid(self) -> float:
        '''
        Central tendancy (median for Nums, mode for Syms)
        '''
        return self.per(self.nums(), 0.5)
