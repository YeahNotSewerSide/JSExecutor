from . import Types
import Exceptions
from .CodeBlock import index_check,CodeBlock
#from StandartTypes import Array

'''
operation - ()

operations:
    ('var',variable_name,(one,two,+,...)) / (1,2,3),func 
                                          / (1,2)|1,list
                                          / ClassAccess('object name','variable/function'))
    ('var_change',variable_name,(one,two,+,...)) / variable_name = ''|variable name=()
    ('let',variable_name,(one,two,+,...))
    ('function',function_name,(input_arguments),(operations))
    ('loop',Loop())
    ('return',(one,two,+,...))
    ('if',If())
        ('if_condition',(one,two,+,...))
    ('try',Try())
'''

#def index_check(input):
#    if isinstance(input,float):
#        if input.is_integer():
#            return int(input)
#    return input

class Function(CodeBlock):
    def __init__(self,input_arguments:list,
                 operations:list,
                 default_values={},
                 nested=False,
                 static=False):
        '''
        input_arguments - (name1,name2,name3)
        default_values - {'name1':default_value}
        '''
        self.input_arguments = tuple(input_arguments)
        self.default_values = default_values
        self.operations = tuple(operations)
        self.nested = nested  
        self.static = static

    def execute(self,arguments,global_variables:dict):
        
        local_variables = {'arguments':arguments,}
        arguments_native = arguments#arguments.this['value']

        if len(self.input_arguments) >=\
           len(arguments_native):
            for argument in enumerate(arguments_native):            
                local_variables[self.input_arguments[argument[0]]] = argument[1]
        
            for i in range(len(arguments_native),\
                            len(self.input_arguments)):
                try:
                    local_variables[self.input_arguments[i]] = self.default_values[self.input_arguments[i]]
                except:
                    local_variables[self.input_arguments[i]] = Types.undefined
        else:
            for input_argument in enumerate(self.input_arguments):
                local_variables[input_argument[1]] = arguments_native[input_argument[0]]

        return_value = Types.undefined
        for operation in self.operations:
            if operation[0] == 'var':
                result = self.calc_operation(operation[2],\
                                        global_variables,\
                                        local_variables)
                local_variables[operation[1]] = result
            elif operation[0] == 'var_change':
                index = self.calc_operation(operation[1],\
                                            global_variables,\
                                            local_variables)
                result = self.calc_operation(operation[2],\
                                        global_variables,\
                                        local_variables)
                if isinstance(index,tuple):
                    data = self.get_variable(index[0],
                                             global_variables,
                                             local_variables)
                    for layer in index[1:-1]:
                        new_index = index_check(layer)
                        try:
                            data = data[new_index]
                        except:
                            raise Exceptions.ReferenceError(new_index)

                    new_index = index_check(index[-1])
                    try:
                        data[new_index] = result 
                    except:
                        raise Exceptions.ReferenceError(new_index)
                else:
                    self.change_variable(index,
                                         result,
                                         global_variables,
                                         local_variables)

            elif operation[0] == 'let':
                result = self.calc_operation(operation[2],\
                                        global_variables,\
                                        local_variables)
                local_variables[operation[1]] = result
                
            elif operation[0] == 'function':
                local_variables[operation[1]] = Function(operation[2],operation[3],nested=True) 

            elif operation[0] == 'if'\
                or operation[0] == 'loop'\
                or operation[0] == 'try':
                global_copy = global_variables.copy()
                global_copy.update(local_variables)
                result = operation[1].execute(global_copy)
                if isinstance(result,tuple):
                    for key in result[1].keys():
                        try:
                            self.change_variable(key,
                                                 result[1][key],
                                                 global_variables,
                                                 local_variables)
                        except:
                            local_variables[key] = result[1][key]
            
                    if self.nested:
                        return result[0],global_variables
                    else:
                        return result[0]
                else:
                    for key in result.keys():
                        try:
                            self.change_variable(key,
                                                 result[key],
                                                 global_variables,
                                                 local_variables)
                        except:
                            local_variables[key] = result[key]

            elif operation[0] == 'return':
                result = self.calc_operation(operation[1],\
                                            global_variables,\
                                            local_variables)
                if self.nested:
                    return result,global_variables
                else:
                    return result

        if self.nested:
            return None,global_variables
        else:
            return None

    def typeof(self):
        return 'function'
                





if __name__ == '__main__':
    #operations = (('if',Types.If((('if_condition',(5,2,Types.LESS_)),\
    #                              ('var','something',(999,1,'+')),\
    #                              ('if_condition',(5,5,Types.EQUAL_)),\
    #                              ('return',('PPP',))
    #                              )
    #                             )
    #               ),
    #              )

    #operations = (('var','a',(0,)),
    #              ('loop',Types.Loop((Types.VarName('a'),5,Types.LESS_),
    #                                 (('var_change','a',(Types.VarName('a'),
    #                                                    1,
    #                                                    Types.PLUS_)),
    #                                  ('return',(((4,3,Types.MINUS_),),Types.ListName('list'))))
    #                                )
    #               ),
    #               ('return',(Types.VarName('a'),))
    #            )

    operations = (('var','a',(('12',),int)),
                  ('return',(Types.VarName('a'),))
        )

    function = Function(('one','two','three'),operations)
    ret = function.execute((1,),{})
    print(ret)