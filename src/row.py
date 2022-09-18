


class Row:
    '''
    Class `Row` holds one record 
    '''

    def __init__(self, t):
        
        '''
        Arguments
        ----------
        t : row in dictionary
        '''
        self.cells = t
        '''Holds one record.'''
        self.cooked = copy(t)
        '''Used if we discretize the data'''
        self.isEvalved = False
        '''True if y-values evaluated'''


###Lists



def copy(t: dict):
    '''
    deepcopy lists additional helper functions
    '''
    u = []
    if type(t) != dict:
        return t
    for key in list(t.keys()):
        u.append(copy(t[key]))

    return u
