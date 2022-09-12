'''
Class Row holds one record 
'''


class Row:
    '''
    Constuctor which initializes the attributes

    Attributes:
    @cells: one record
    @cooked: used if we discretize data
    @isEvalved: true if y-values evaluated

    Arguments:
    @t: row in dictionary
    '''

    def __init__(self, t):
        self.cells = t
        self.cooked = copy(t)
        self.isEvalved = False


###Lists
'''
deepcopy lists additional helper functions
'''


def copy(t: dict):
    u = []
    if type(t) != dict:
        return t
    for key in list(t.keys()):
        u.append(copy(t[key]))

    return u
