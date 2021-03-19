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


#class Bool:
#    def __init__(self,a:bool):
#        self.flag = bool(a)

#    def __bool__(self):
#        return self.flag
#    def __int__(self):
#        if self.flag:
#            return 1
#        else:
#            return 0
#    def __float__(self):
#        return self.__int__()
#    def __str__(self):
#        if self.flag:
#            return 'true'
#        else:
#            return 'false'
#    def __repr__(self):
#        return self.__str__()

#    def typeof(self):
#        return 'boolean'

#preallocated booleans
#True_ = Bool(True)
#False_ = Bool(False)



#class ClassExecute(tuple):
#    def __new__ (cls, b):
#        return super(ClassExecute, cls).__new__(cls, tuple(b))

class ClassExecute:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

class ClassNew:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

#class ClassAccess(tuple):
#    def __init__(self,*args):
#        super().__init__(args)

#class ClassNew:
#    def __init__(self,name):
#        self.name = name
#    def __str__(self):
#        return self.name
#    def __repr__(self):
#        return self.name

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
EXECUTE_ = Operation('exe')










if __name__ == '__main__':
    vr = VarName('123')
    print(vr)
