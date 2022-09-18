import math

class Sym:
    '''
    Class `Sym` which handles symmbolic characters
    '''
   

    def __init__(self, c=0, s=""):
        '''    
        Arguments
        ----------
        c : Column position
        s : Column name
        '''
        self.n = 0
        '''Items seen.'''
        self.at = c + 1
        '''Column position.'''
        self.name = s
        '''Column Name.'''
        self._has = {}
        '''Kept data.'''



    def add(self, v):
        '''
        Adding value to _has dictionary
    
        Arguments
        ----------
        v : Value to be added
        '''
        if v != "?":
            self.n += 1
            if (v not in self._has.keys()):
                self._has[v] = 1
            else:
                self._has[v] += 1


    def mid(self) -> str:
        '''
        Finding mode of the dictionary
        '''
        most = -1
        for i in self._has:
            if (self._has[i] > most):
                mode = i
                most = self._has[i]
        return mode


    def entropy(self, p):
        '''
        Entropy Formula
        '''
        return (p*math.log2(p))


    def div(self) -> float:
        '''
        Calculates the diversity of each variable using entropy formula
        '''
        e = 0
        for i in self._has:
            if self._has[i] > 0:
                e = e-(self.entropy(self._has[i]/self.n))
        return round(e, 3)
