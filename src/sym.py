import math

'''
Class Sym which handles symmbolic characters 
'''


class Sym:
    '''
    Constuctor which initializes the attributes

    Attributes:
    @n: items seen
    @at: column position
    @name: column name
    @_has: kept data

    Arguments:
    @c: column postition
    @s: column name
    '''

    def __init__(self, c=0, s=""):
        self.n = 0
        self.at = c + 1
        self.name = s
        self._has = {}

    '''
    Adding value to _has dictionary
    
    Arguments
    @v: Value being added
    '''

    def add(self, v):
        if v != "?":
            self.n += 1
            if (v not in self._has.keys()):
                self._has[v] = 1
            else:
                self._has[v] += 1

    '''
    Finding mode of the dictionary

    @most: Most number of occurrences out of all keys present in the _has dictionary
    @mode: Element which has occurred most number of times
    '''

    def mid(self) -> str:
        most = -1
        for i in self._has:
            if (self._has[i] > most):
                mode = i
                most = self._has[i]
        return mode

    '''
    Entropy Formula
    '''

    def entropy(self, p):
        return (p*math.log2(p))

    '''
    Calculates the diversity of each variable using entropy formula

    @e: Entropy
    '''

    def div(self) -> float:
        e = 0
        for i in self._has:
            if self._has[i] > 0:
                e = e-(self.entropy(self._has[i]/self.n))
        return round(e, 3)
