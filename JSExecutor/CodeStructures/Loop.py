from . import Types
import Exceptions
from .CodeBlock import CodeBlock

'''
operation - ()

operations:
    ('var',variable_name,(one,two,+,...)) / (1,2,3),func / (1,2)|1,list
    ('var_change',variable_name,(one,two,+,...)) / variable_name = ''|variable name=()
    ('let',variable_name,(one,two,+,...))
    ('function',function_name,(input_arguments),(operations))
    ('loop',Loop())
    ('return',(one,two,+,...))
    ('if',If())
        ('if_condition',(one,two,+,...))
    ('try',Try())
    ('continue',)
'''


class Loop(CodeBlock):
    def __init__(self,stop_condition:tuple,operations:tuple,nested=False):
        '''
        stop_condition - (2,3,+)
        '''
        self.stop_condition = stop_condition
        self.operations = operations
        self.nested = nested


    def execute(self,global_variables:dict):
        local_variables = {}
        while bool(self.calc_operation(self.stop_condition,global_variables,local_variables)):
            for operation in self.operations:
                if operation[0] == 'var':
                    result = self.calc_operation(operation[2],\
                                            global_variables,\
                                            local_variables)
                    global_variables[operation[1]] = result
                elif operation[0] == 'var_change':
                    result = self.calc_operation(operation[2],\
                                        global_variables,\
                                        local_variables)
                    if isinstance(operation[1],str):
                        try:
                            res = local_variables[operation[1]]
                            local_variables[operation[1]] = result
                        except:
                            try:
                                res = global_variables[operation[1]]
                                global_variables[operation[1]] = result
                            except:
                                raise Exceptions.ReferenceError(operation[1])
                    else:
                        if isinstance(operation[1][0],tuple):
                            index = self.calc_operation(operation[1][0],global_variables,local_variables)
                        else:
                            index = operation[1][0]
                        try:
                            data = local_variables[index]
                        except:
                            try:
                                data = global_variables[index]
                            except:
                                raise Exceptions.ReferenceError(index)
                    
                        for layer in operation[1][1:-1]:
                            if isinstance(layer,tuple):
                                index = self.calc_operation(layer,global_variables,local_variables)
                            else:
                                index = layer
                            try:
                                data = data[index]
                            except:
                                raise Exceptions.ReferenceError(index)
                        if isinstance(operation[1][-1],tuple):
                            index = self.calc_operation(operation[1][-1],global_variables,local_variables)
                        else:
                            index = operation[1][-1]
                        data[operation[1][-1]] = result
                elif operation[0] == 'let':
                    result = self.calc_operation(operation[2],\
                                        global_variables,\
                                        local_variables)
                    local_variables[operation[1]] = result
                elif operation[0] == 'function':
                    global_variables[operation[1]] = Types.Function(operation[2],operation[3],True)
                elif operation[0] == 'if':
                    global_copy = global_variables.copy()
                    global_copy.update(local_variables)
                    result = operation[1].execute(global_copy)
                    if isinstance(result,tuple):
                        return result

                elif operation[0] == 'loop':
                    global_copy = global_variables.copy()
                    global_copy.update(local_variables)
                    result = operation[1].execute(global_copy)
                    if isinstance(result,tuple):
                        return result

                elif operation[0] == 'try':                    
                    global_copy = global_variables.copy()
                    global_copy.update(local_variables)
                    result = operation[1].execute(global_copy)
                    if isinstance(result,tuple):
                        return result
                    
                elif operation[0] == 'return':
                    result = self.calc_operation(operation[1],\
                                            global_variables,\
                                            local_variables)
                    return result,global_variables
                elif operation[0] == 'continue':
                    break

        return global_variables