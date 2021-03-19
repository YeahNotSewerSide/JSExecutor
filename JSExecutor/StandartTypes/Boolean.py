import inspect

methods = None



class Boolean_object:
    def __init__(self,a=None):
        self.flag = bool(a)

    def __bool__(self):
        return self.flag
    def __int__(self):
        if self.flag:
            return 1
        else:
            return 0
    def __float__(self):
        return self.__int__()
    def __str__(self):
        if self.flag:
            return 'true'
        else:
            return 'false'

    def toString(self):
        return str(self)

    def valueOf(self):
        return self

    def __repr__(self):
        return self.__str__()

    def typeof(self):
        return 'boolean'

    def execute_function(self,\
                        function_name:str,\
                        arguments:tuple,\
                        global_variables:dict):
        global methods
        return methods[function_name](self)

methods = dict(inspect.getmembers(Boolean_object, predicate=inspect.isfunction))

class Boolean_mother:
    def new(self,input,global_parameters):
        return Boolean_object(input[0])

Boolean = Boolean_mother()

#Bool = Types.Class('')
