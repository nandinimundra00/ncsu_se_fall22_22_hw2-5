import re
from  src.Num import Num
from  src.sym import Sym

'''
Class `Cols` Summarizes the first row of the dataset
'''

class Cols:
    '''
    Constuctor which initializes the attributes

    Attributes:
    @names: column names
    @all: storing Num or Sym objects
    @klass: the single dependent class if it exists
    @x: independent columns
    @y: dependent columns

    Arguments:
    @names: column names
    '''
    def __init__(self, names, the) -> None:
        self.names = names 
        self.all = []
        self.klass = None
        self.x = []
        self.y = []

        '''
        First, storing all the Num and Sym Objects into the "all" attribute
        Second, performing regex to separate the dependent from independent variables into the attributes "y" and "x"
        respectively
        For the atributes "x" and "y" we skip all columns which end with ":".
        '''
        for i in range(len(names)):
            if(re.search("^[A-Z]", names[i])):
                self.all.append(Num(the, i, names[i]))
            else:
                self.all.append(Sym(i, names[i]))
            
            if(not re.search(":$", names[i])):
                if(re.search("\+$", names[i])):
                    self.x.append(self.all[i])
                elif(re.search("\-$", names[i])):
                    self.y.append(self.all[i])

                if(re.search("!$", names[i])):
                    self.klass = self.all[i]



''' Can remove after testing, just to see the values outputted from the variables'''
# def showStats():
#     li = ["Clndrs","Volume","Hp:","Lbs-","Acc+","Model","origin","Mpg+"]
        
#     cols = Cols(li,{"seed":2})

#     # print(cols.all)
#     for i in cols.all:
#         print(i.name, " ", i)
    
#     print("-"*100)
#     for i in cols.x:
#         print(i.name)
#     # print(cols.x)
#     # print(cols.y)
#     print("-"*100)
#     for i in cols.y:
#         print(i.name)
#     print("-"*100)
#     print(cols.names)
#     print(cols.klass)

            

# showStats()
