from . import Types
import Exceptions
import VMExceptions

import StandartTypes

def index_check(input):
    #if isinstance(input,float):
    #    if input.is_integer():
    #        return int(input)
    #return input
    if not isinstance(input,str) \
        and str(input.typeof()) == 'number':
        if input.this['value'].is_integer():
            return int(input)
        else:
            return float(input)
    else:
        return str(input)
    #if not isinstance(input,str)\
    #    and str(input.typeof()) == 'number'\
    #    and isinstance(input.this['value'],float)\
    #    and input.this['value'].is_integer():
    #        return int(input)
    #elif str(input.typeof()) == 'number':
    #    return float(input)
    #else:
    #    return str(input)
    


class CodeBlock:
    def get_variable(self,name,\
                     global_variables:dict,\
                     local_variables:dict):

        try:
            data = local_variables[name]
        except:
            try:
                data = global_variables[name]
            except:
                raise Exceptions.ReferenceError(name)
        return data

    def change_variable(self,\
                        name,\
                        value,\
                        global_variables:dict,\
                        local_variables:dict):
        try:
            data = local_variables[name]
            local_variables[name] = value
        except:
            try:
                data = global_variables[name]
                global_variables[name] = value
            except:
                raise Exceptions.ReferenceError(name)

    def calc_operation(self,operation:tuple,\
                        global_variables:dict,\
                        local_variables:dict):
        stack = []
        for item in operation:
            result = None  
            if isinstance(item,Types.VarName):
                try:
                    result = local_variables[str(item)]
                except:
                    try:
                        result = global_variables[str(item)]
                    except:
                        raise Exceptions.ReferenceError(str(item))
            elif isinstance(item,Types.Operation):
                if item == Types.PLUS_:
                    second = stack.pop()
                    first = stack.pop() 
                    if isinstance(first,tuple):
                        first = self.calc_operation(first,\
                                                    global_variables,\
                                                    local_variables)
                    if isinstance(second,tuple):
                        second = self.calc_operation(second,\
                                                    global_variables,\
                                                    local_variables)
                    if first.typeof() == 'string'\
                       or second.typeof() == 'string':
                        first_string = str(first.execute_function('toString',(),
                                                              global_variables))
                        second_string = str(second.execute_function('toString',(),
                                                              global_variables))
                        native_string_wrapped = StandartTypes.String.string_native(first_string+second_string)
                        result = StandartTypes.String.String.new((native_string_wrapped,),
                                                                 global_variables)
                    else:
                        if first == Types.NaN or second == Types.NaN:
                            result = Types.NaN
                        elif first == Types.undefined or second == Types.undefined:
                            result = Types.NaN
                        else:
                            result = StandartTypes.Number.Number.new((float(first) + float(second),),
                                                                     global_variables)
                
                elif item == Types.MINUS_:
                    second = stack.pop()
                    first = stack.pop()
                    if isinstance(first,tuple):
                        first = self.calc_operation(first,\
                                                    global_variables,\
                                                    local_variables)
                    if isinstance(second,tuple):
                        second = self.calc_operation(second,\
                                                    global_variables,\
                                                    local_variables)
                    try:
                        result = StandartTypes.Number.Number.new((float(first) - float(second),),
                                                                     global_variables)
                    except:
                        result = Types.NaN
                
                elif item == Types.MULT_:
                    second = stack.pop()
                    first = stack.pop()
                    if isinstance(first,tuple):
                        first = self.calc_operation(first,\
                                                    global_variables,\
                                                    local_variables)
                    if isinstance(second,tuple):
                        second = self.calc_operation(second,\
                                                    global_variables,\
                                                    local_variables)
                    try:
                        result = StandartTypes.Number.Number.new((float(first) * float(second),),
                                                                     global_variables)
                    except:
                        result = Types.NaN
                
                elif item == Types.DIVISION_:
                    second = stack.pop()
                    first = stack.pop()
                    if isinstance(first,tuple):
                        first = self.calc_operation(first,\
                                                    global_variables,\
                                                    local_variables)
                    if isinstance(second,tuple):
                        second = self.calc_operation(second,\
                                                    global_variables,\
                                                    local_variables)
                    try:
                        result = StandartTypes.Number.Number.new((float(first)/float(second),),
                                                                     global_variables)
                    except:
                        result = Types.NaN
                
                elif item == Types.POWER_:
                    second = stack.pop()
                    first = stack.pop()
                    if isinstance(first,tuple):
                        first = self.calc_operation(first,\
                                                    global_variables,\
                                                    local_variables)
                    if isinstance(second,tuple):
                        second = self.calc_operation(second,\
                                                    global_variables,\
                                                    local_variables)
                    try:
                        result = StandartTypes.Number.Number.new((float(first)**float(second),),
                                                                 global_variables)
                    except:
                        result = Types.NaN
                
                elif item == Types.EQUAL_:
                    second = stack.pop()
                    first = stack.pop()
                    if isinstance(first,tuple):
                        first = self.calc_operation(first,\
                                                    global_variables,\
                                                    local_variables)
                    if isinstance(second,tuple):
                        second = self.calc_operation(second,\
                                                    global_variables,\
                                                    local_variables)
                    try:
                        if str(first.typeof()) == 'number' or\
                           str(second.typeof()) == 'number':
                            result = float(first)==float(second)
                        else:
                            result = str(first.execute_function('toString',(),global_variables)) == \
                                    str(second.execute_function('toString',(),global_variables))
                    except:
                        result = str(first.execute_function('toString',(),global_variables)) == \
                                    str(second.execute_function('toString',(),global_variables))
                    result = StandartTypes.Boolean.Boolean.new((result,),global_variables)
                    
                elif item == Types.STRICTEQUAL_:
                    second = stack.pop()
                    first = stack.pop()
                    if isinstance(first,tuple):
                        first = self.calc_operation(first,\
                                                    global_variables,\
                                                    local_variables)
                    if isinstance(second,tuple):
                        second = self.calc_operation(second,\
                                                    global_variables,\
                                                    local_variables)
                    if str(first.typeof()) != str(second.typeof()):
                        result = False
                    else:
                        result = str(first.execute_function('toString',(),global_variables)) == \
                                 str(second.execute_function('toString',(),global_variables))
                    result = StandartTypes.Boolean.Boolean.new((result,),global_variables)
                elif item == Types.MORE_:
                    second = stack.pop()
                    first = stack.pop()
                    if isinstance(first,tuple):
                        first = self.calc_operation(first,\
                                                    global_variables,\
                                                    local_variables)
                    if isinstance(second,tuple):
                        second = self.calc_operation(second,\
                                                    global_variables,\
                                                    local_variables)
                    try:
                        result = StandartTypes.Boolean.Boolean.new((float(first)>float(second),),
                                                                     global_variables)
                    except:
                        result = StandartTypes.Boolean.Boolean.new((False,),
                                                                     global_variables)
                elif item == Types.MOREEQUAL_:
                    second = stack.pop()
                    first = stack.pop()
                    if isinstance(first,tuple):
                        first = self.calc_operation(first,\
                                                    global_variables,\
                                                    local_variables)
                    if isinstance(second,tuple):
                        second = self.calc_operation(second,\
                                                    global_variables,\
                                                    local_variables)
                    try:
                        if str(first.typeof()) == 'number' or\
                           str(second.typeof()) == 'number':
                            result = float(first)>=float(second)
                        else:
                            result = str(first.execute_function('toString',(),global_variables)) >= \
                                    str(second.execute_function('toString',(),global_variables))
                    except:
                        result = str(first.execute_function('toString',(),global_variables)) >= \
                                    str(second.execute_function('toString',(),global_variables))
                    result = StandartTypes.Boolean.Boolean.new((result,),global_variables)

                elif item == Types.LESS_:
                    second = stack.pop()
                    first = stack.pop()
                    if isinstance(first,tuple):
                        first = self.calc_operation(first,\
                                                    global_variables,\
                                                    local_variables)
                    if isinstance(second,tuple):
                        second = self.calc_operation(second,\
                                                    global_variables,\
                                                    local_variables)
                    try:
                        result = StandartTypes.Boolean.Boolean.new((float(first)<float(second),),
                                                                     global_variables)
                    except:
                        result = StandartTypes.Boolean.Boolean.new((False,),
                                                                     global_variables)

                elif item == Types.LESSEQUAL_:
                    second = stack.pop()
                    first = stack.pop()
                    if isinstance(first,tuple):
                        first = self.calc_operation(first,\
                                                    global_variables,\
                                                    local_variables)
                    if isinstance(second,tuple):
                        second = self.calc_operation(second,\
                                                    global_variables,\
                                                    local_variables)
                    try:
                        if str(first.typeof()) == 'number' or\
                           str(second.typeof()) == 'number':
                            result = float(first)<=float(second)
                        else:
                            result = str(first.execute_function('toString',(),global_variables)) <= \
                                    str(second.execute_function('toString',(),global_variables))
                    except:
                        result = str(first.execute_function('toString',(),global_variables)) <= \
                                    str(second.execute_function('toString',(),global_variables))
                    result = StandartTypes.Boolean.Boolean.new((result,),global_variables)
                
                elif item == Types.RIGHTSHIFT_:
                    second = stack.pop()
                    first = stack.pop()
                    if isinstance(first,tuple):
                        first = self.calc_operation(first,\
                                                    global_variables,\
                                                    local_variables)
                    if isinstance(second,tuple):
                        second = self.calc_operation(second,\
                                                    global_variables,\
                                                    local_variables)
                    try:
                        result = StandartTypes.Number.Number.new((int(first)>>int(second),),
                                                                     global_variables)
                    except:
                        try:
                            number_native = int(first)
                            try:
                                int(second)
                                number_native = 0
                            except:
                                pass
                        except:
                            number_native = 0
                        result = StandartTypes.Number.Number.new((number_native,),
                                                                   global_variables)
                elif item == Types.USIGNEDRIGTHSHIFT_:
                    second = stack.pop()
                    first = stack.pop()
                    if isinstance(first,tuple):
                        first = self.calc_operation(first,\
                                                    global_variables,\
                                                    local_variables)
                    if isinstance(second,tuple):
                        second = self.calc_operation(second,\
                                                    global_variables,\
                                                    local_variables)

                    try:
                        first_native = int(first)
                        second_native = int(second)
                        if first_native<0:
                            first_native *= -1
                        result = StandartTypes.Number.Number((first_native>>second_native,),
                                                             global_variables)
                    except:
                        try:
                            number_native = int(first)
                            try:
                                int(second)
                                number_native = 0
                            except:
                                pass
                        except:
                            number_native = 0
                        result = StandartTypes.Number.Number.new((number_native,),
                                                                   global_variables)
                elif item == Types.LEFTSHIFT_:
                    second = stack.pop()
                    first = stack.pop()
                    if isinstance(first,tuple):
                        first = self.calc_operation(first,\
                                                    global_variables,\
                                                    local_variables)
                    if isinstance(second,tuple):
                        second = self.calc_operation(second,\
                                                    global_variables,\
                                                    local_variables)
                    try:
                        result = StandartTypes.Number.Number.new((int(first)<<int(second),),
                                                                     global_variables)
                    except:
                        try:
                            number_native = int(first)
                            try:
                                int(second)
                                number_native = 0
                            except:
                                pass
                        except:
                            number_native = 0
                        result = StandartTypes.Number.Number.new((number_native,),
                                                                   global_variables)
                elif item == Types.NOT_:
                    first = stack.pop()
                    if isinstance(first,tuple):
                        first = self.calc_operation(first,\
                                                    global_variables,\
                                                    local_variables)
                    first.flag = not first.flag
                    result = first
                elif item == Types.EXECUTE_:
                    func = stack.pop()
                    count_of_arguments = stack.pop()

                    if not isinstance(count_of_arguments,int):
                        raise VMExceptions.WrongCountOfArguments()

                    arguments_calculated = []
                    for i in range(count_of_arguments):
                        arguments_calculated.append(stack.pop())

                    if isinstance(func,Types.Function):
                        merged_global_variables = global_variables.copy()
                        merged_global_variables.update(local_variables)
                        result = func.execute(arguments_calculated,merged_global_variables)
                        if func.nested:
                            for key in result[1].keys():
                                try:
                                    local_variables[key]
                                    local_variables[key] = result[1][key]
                                except:
                                    try:
                                        global_variables[key]
                                        global_variables[key] = result[1][key]
                                    except:
                                        pass
                            result = result[1]
                    elif isinstance(func,Types.ClassExecute):
                        object = stack.pop()
                        result = object.execute_function(str(func),
                                                         arguments_calculated,
                                                         global_variables)
                    elif callable(func):
                        result = func(*arguments_calculated)
                elif item == Types.NEW_:
                    class_ = stack.pop()
                    count_of_arguments = stack.pop()
                    if not isinstance(count_of_arguments,int):
                        raise VMExceptions.WrongCountOfArguments()

                    arguments_calculated = []
                    for i in range(count_of_arguments):
                        arguments_calculated.append(stack.pop())
                    result = class_.new(arguments_calculated,
                                        global_variables)
                elif item == Types.LISTACCESS_:
                    result = stack.pop()
                    indexes_count = stack.pop()
                    for i in range(indexes_count):
                        index = index_check(stack.pop())
                        result = result[index]


            else:
                result = item
            stack.append(result)
        
        if len(stack)>1:
            return tuple(stack)
        else:
            return stack.pop()
