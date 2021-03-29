from . import Types
import Exceptions
from .CodeBlock import CodeBlock



class Class:
    def __init__(self,name:str,
                 constructor:Types.Function,
                 variables:dict):
        '''
        constructor - function
        methods = {'funcName':Function()}
        '''
        self.name = name
        self.constructor = constructor
        #self.methods = methods
        self.variables = variables

    def new(self,arguments:tuple,global_variables:dict):
        '''
        if constructor returns NaN, then new will return NaN
        if constructor returns something different from NaN, will return object
        '''
        global_variables['this.'] = self.variables.copy()
        result = self.constructor.execute(arguments,global_variables)
        if result == Types.NaN:
            return result
        obj = Object(self,global_variables['this.'])
        return obj
    def get_name(self):
        return self.name






class Object(CodeBlock):
    def __init__(self,prototype:Class,this:dict,extends=False):
        '''
        extends - Class()
        '''

        self.prototype = prototype
        self.extends = extends
        self.this = this
        self.this['this.'] = self

    def get_attribute(self,attribute_name):
        try:
            return self.this[attribute_name]
        except:
            if self.extends != False:
                return self.extends.get_attribute(attribute_name)
            else:
                return Types.undefined
                #try:
                #    return self.MotherClass.methods[attribute_name]
                #except:
                #    #raise Exceptions.AttributeError(self.MotherClass.name,
                #    #                                attribute_name)
                #    return Types.undefined
    def execute_function(self,\
                        function_name:str,\
                        arguments:tuple,\
                        global_variables:dict):
        function = self.get_attribute(function_name)
        
        result = None
        if isinstance(function,Types.Function):
            if function.static:
                result = function.execute(arguments,global_variables)
            else:            
                list_arguments = list(arguments)
                list_arguments.insert(0,self.this)
                result = function.execute(list_arguments,global_variables)
        elif callable(function):
            result = function(*arguments)
        else:
            raise Exceptions.NotCallable(function)

        return result

    def __getitem__(self, key):
        return self.get_attribute(key)

    def __str__(self):
        '''
        *magic* functions work only with self.this['value']
        '''
        return str(self.this['value'])

    def __repr__(self):
        return str(self)

    def __float__(self):
        return float(self.this['value'])
    def is_int(self):
        return self.this['value'].is_integer()

    def __int__(self):
        return int(self.this['value'])

    def __bool__(self):
        return bool(self.this['value'])
    


    def typeof(self):
        return self.prototype.get_name()



if __name__ == '__main__':
    constructor = Types.Function(('first','second'),
                                 (('var_change',('this.','list'),([1,2,3,4],)),
                                  ('var_change',('this.','IDK'),(5,9,Types.MINUS_)),
                                  ('var_change',('this.','IDK'),(('IDK',),Types.ListName('this.'),9,Types.PLUS_)),
                                  #('return',(Types.VarName('this.'),))
                                  )
                                 )
    cl = Class('class',constructor,{})
    new_obj = cl.new(tuple(),{})
    res = new_obj.get_attribute('list')
    print(new_obj)
