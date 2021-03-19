from . import Types
import Exceptions
from .CodeBlock import CodeBlock


'''
branches:
    (('try')(operations)('catch',var_exception_name)(operations)('finally')(operations))

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
    
'''


class Try(CodeBlock):
    def __init__(self,branches:tuple):
        self._try = []
        self._catch = []
        self._finaly = []

        branch_number = -1

        for branch in branches:
            if branch[0] == 'try':
                branch_number = 0
            elif branch[0] == 'catch':
                branch_number = 1
            elif branch[0] == 'finally':
                branch_number = 2
            else:
                if branch_number == 0:
                    self._try.append(branch)
                elif branch_number == 1:
                    self._catch.append(branch)
                elif branch_number == 2:
                    self._finally.append(branch)    

    def execute(self,global_variables:dict):
        local_variables = {}
        
        exception_fired_try = False
        exception_try = None

        exception_fired_catch = False
        exception_catch = None

        global_copy = None

        for operation in self._try:
            
            try:
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
            except Exceptions as e:
                exception_fired_try = True
                exception_try = e


        if exception_fired_try:
            for operation in self._catch:
                try:
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
                        if global_copy == None:
                            global_copy = global_variables.copy()
                            global_copy.update(local_variables)
                        result = operation[1].execute(global_copy)
                        if isinstance(result,tuple):
                            return result
                        
                    elif operation[0] == 'loop':
                        if global_copy == None:
                            global_copy = global_variables.copy()
                            global_copy.update(local_variables)
                        result = operation[1].execute(global_copy)
                        if isinstance(result,tuple):
                            return result

                    elif operation[0] == 'try':
                        if global_copy == None:
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

                except Exceptions as e:
                    exception_fired_catch = True
                    exception_catch = e


        for operation in self._finaly:            
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
                if global_copy == None:
                    global_copy = global_variables.copy()
                    global_copy.update(local_variables)
                result = operation[1].execute(global_copy)
                if isinstance(result,tuple):
                    return result
                        
            elif operation[0] == 'loop':
                if global_copy == None:
                    global_copy = global_variables.copy()
                    global_copy.update(local_variables)
                result = operation[1].execute(global_copy)
                if isinstance(result,tuple):
                    return result

            elif operation[0] == 'try':
                if global_copy == None:
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


        if global_copy != None:
            for key in global_copy.keys():
                try:
                    local_variables.get(key)
                    local_variables[key] = global_copy[key]
                except:
                    try:
                        global_variables.get(key)
                        global_variables[key] = global_copy[key]
                    except:
                        local_variables[key] = global_copy[key]


        if exception_fired_catch:
            raise exception_catch
        elif exception_fired_try:
            pass
            #raise exception_fired_catch

        return global_variables
        




