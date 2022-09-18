import re
from  src.Num import Num
from  src.sym import Sym



class Cols:
    '''
    Class for `Columns`
    First, all the `Num` and `Sym` Objects are stored into into the `all` attribute. \n
    Secondly, performing regex to separate the dependent from independent variables into the attributes `y` and `x`
    respectively.\n
    For the atributes `x` and `y` we skip all columns which end with ":".
    '''

    def __init__(self, names, the) -> None:
        '''
        Arguments
        ----------
        names : Column Names to be added 
        the : Configuration variable of the command line interface
        '''
        self.names = names
        '''Column Names''' 
        self.all = []
        '''Storing Num or Sym objects'''
        self.klass = None
        '''The single dependent class if it exists'''
        self.x = []
        '''Independent Columns'''
        self.y = []
        '''Dependent Columns'''

        for i in range(len(names)):
            if(re.search("^[A-Z]", names[i])):
                self.all.append(Num(the, i, names[i]))
            else:
                self.all.append(Sym(i, names[i]))
            
            if(not re.search(":$", names[i])):
                if(re.search("[\+\-]$", names[i])):
                    self.y.append(self.all[i])
                else:
                    self.x.append(self.all[i])

                if(re.search("!$", names[i])):
                    self.klass = self.all[i]
