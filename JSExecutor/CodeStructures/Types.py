from .Undefined import Undefined
from .Function import Function
from .Loop import Loop
from .If import If
from .Class import Class
#from StandartTypes.Bool import Bool


undefined = Undefined()


class NaN_:
    def __init__(self):
        pass

    def __str__(self):
        return 'NaN'
    def __repr__(self):
        return 'NaN'

NaN = NaN_()

class Null(int):
    def __str__(self):
        return 'null'
    def __repr__(self):
        return 'null'
    def __bool__(self):
        return False
    def typeof(self):
        return 'object'

null = Null(0)

def isNaN(inp='g'):
    try:
        int(inp)
        return False
    except:
        return True

class ClassExecute:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


class VarName:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


'''
ListName used for access data in lists and classes
'''
class ListName:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

class Operation:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


#preallocated operations:
PLUS_ = Operation('+')
MINUS_ = Operation('-')
MULT_ = Operation('*')
DIVISION_ = Operation('/')
POWER_ = Operation('**')
EQUAL_ = Operation('==')
STRICTEQUAL_ = Operation('===')
RIGHTSHIFT_ = Operation('>>')
USIGNEDRIGTHSHIFT_ = Operation('>>>')
LEFTSHIFT_ = Operation('<<')
NOT_ = Operation('!')
MORE_ = Operation('>')
LESS_ = Operation('<')
MOREEQUAL_ = Operation('>')
LESSEQUAL_ = Operation('<')
EXECUTE_ = Operation('exe')
NEW_ = Operation('new')
LISTACCESS_ = Operation('list')










if __name__ == '__main__':
    vr = VarName('123')
    print(vr)
