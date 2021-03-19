from . import Types
import Exceptions
import StandartTypes

def index_check(input):
    #if isinstance(input,float):
    #    if input.is_integer():
    #        return int(input)
    #return input
    if not isinstance(input,tuple)\
        and not isinstance(input,str)\
        and str(input.typeof()) == 'number'\
        and isinstance(input.this['value'],float)\
        and input.this['value'].is_integer():
            return int(input)
    else:
        return input
    


class CodeBlock:
    def calc_operation(self,operation:tuple,\
                        global_variables:dict,\
                        local_variables:dict):
        stack = []
        for item in operation:
            result = None  
            if isinstance(item,Types.ClassNew):
                try:
                    result = local_variables[str(item)]
                except:
                    try:
                        result = global_variables[str(item)]
                    except:
                        raise Exceptions.ReferenceError(str(item))
                arguments = stack.pop()
                arguments_calculated = []
                for argument in arguments:
                    if isinstance(argument,tuple):
                        arguments_calculated.append(self.calc_operation(argument,\
                                                                     global_variables,\
                                                                     local_variables))
                    else:
                        arguments_calculated.append(argument)
                result = result.new(arguments_calculated,global_variables)
               

            elif isinstance(item,Types.VarName):
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
                    if isinstance(func,tuple):
                        first = self.calc_operation(func,\
                                                    global_variables,\
                                                    local_variables)
                    arguments = stack.pop()
                    arguments_calculated = []
                    for argument in arguments:
                        if isinstance(argument,tuple):
                            arguments_calculated.append(self.calc_operation(argument,\
                                                                         global_variables,\
                                                                         local_variables))
                        else:
                            arguments_calculated.append(argument)
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
                        #try:
                        #    result = local_variables[str(func[0])]
                        #except:
                        #    try:
                        #        result = global_variables[str(func[0])]
                        #    except:
                        #        raise Exceptions.ReferenceError(str(func))
                        result = object.execute_function(str(func),
                                                         arguments_calculated,
                                                         global_variables)
                    elif callable(func):
                        result = func(*arguments_calculated)
            elif isinstance(item,Types.ListName):
                index = index_check(stack.pop())
                if isinstance(index,tuple):
                    try:
                        result = local_variables[str(item)]
                    except:
                        try:
                            result = global_variables[str(item)]
                        except:
                            raise Exceptions.ReferenceError(str(item))
                    for argument in index:
                        calculated_argument = None

                        if isinstance(argument,tuple):
                            calculated_argument = self.calc_operation(argument,\
                                                  global_variables,\
                                                  local_variables)
                        else:
                            calculated_argument = argument
                        
                        result = result[index_check(calculated_argument)]
                else:
                    raise Exceptions.BadListIndex(index)
            #elif isinstance(item,Types.ClassAccess):

            else:
                result = item
            stack.append(result)
        
        if len(stack)>1:
            return tuple(stack)
        else:
            return stack.pop()
