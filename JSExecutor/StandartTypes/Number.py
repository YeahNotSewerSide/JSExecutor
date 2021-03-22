#from Bool import Bool
from CodeStructures import Types
import string
from StandartTypes import String


digs = string.digits + string.ascii_letters


MAX_VALUE = float(1.7976931348623157e+308)
MIN_VALUE = float(5e-324)

MAX_SAFE_INTEGER = 9007199254740991
MIN_SAFE_INTEGER = -9007199254740991

#def isSafeInteger(number):
#    converted = int(number)
#    if converted>=MIN_SAFE_INTEGER \
#        and converted <= MAX_SAFE_INTEGER:
#        return Bool(True)
#    else:
#        return Bool(False)

'''
Number constructor START
'''
def convert_to_number(input):
    try:
        number = float(input)
        return number
    except:
        return Types.NaN


NUMBER_CONSTRUCTOR_OPERATIONS = (('var_change',('this.','value'),
                                  (Types.VarName('input'),
                                   1,
                                   convert_to_number,
                                   Types.EXECUTE_)),

                                 ('return',('value',
                                            1,
                                            Types.VarName('this.'),
                                            Types.LISTACCESS_))
                                 )

NUMBER_CONSTRUCTOR = Types.Function(('input',),
                                    NUMBER_CONSTRUCTOR_OPERATIONS)
'''
Number constructor END
'''


'''
Number class definition START
'''
NUMBER_METHODS = {}

Number = Types.Class(None,NUMBER_CONSTRUCTOR,NUMBER_METHODS)
Number.name = String.String.new((String.string_native('number'),),{})
'''
Number class definition END
'''


'''
toExponential function START
'''
def get_precision(str_value):
    vals =  str_value.split('.')
    if (vals[0] == '0'):
        return len(vals[1])
    else:
        return len(str_value)-2

def clear_output(input:str):
    to_return = ''
    start = input.find('+')+1
    to_return = input[:start]
    for i in range(start,len(input)):
        if input[i] != '0':
            start = i
            break
    to_return += input[start:]
    return String.String.new((String.string_native(to_return),),{})

def toExponential_native(number:float,precision=None):
    to_return = None
    if precision == None or precision == Types.undefined:
        to_return = ('{:.'+str(get_precision(str(number)))+'e}').format(float(number))
    else:
        to_return = ('{:.'+str(precision)+'e}').format(float(number))
    return clear_output(to_return)

toExponential_operations = (('return',
                            (
                                Types.VarName('precision'),
                                'value',
                                1,
                                Types.VarName('this'),
                                Types.LISTACCESS_,
                                 2,
                             toExponential_native,
                             Types.EXECUTE_)
                            ),)

toExponential_wrapper = Types.Function(('this','precision'),
                                      toExponential_operations,
                                      static=False)
'''
toExponential function END
'''

'''
toFixed function START
'''
def toFixed_native(number:float,precision=0):
    if precision == None or precision == Types.undefined:
        precision = 0
    precision = int(precision)
    return String.String.new((String.string_native(
        ('{:.'+str(precision)+'f}').format(float(number))),),{})
    

toFixed_operations = (('return',
                            (
                                Types.VarName('precision'),
                                'value',
                                1,
                                Types.VarName('this'),
                                Types.LISTACCESS_,
                                 2,
                             toFixed_native,
                             Types.EXECUTE_)
                            ),)

toFixed_wrapper = Types.Function(('this','precision'),
                                  toFixed_operations,
                                  static=False)
'''
toFixed function END
'''

'''
toLocaleString function START
'''
def toLocaleString_native(number):
    return String.String.new((String.string_native("{:n}".format(number)),),{})

toLocaleString_operations = (('return',
                                (
                                    'value',
                                    1,
                                    Types.VarName('this'),
                                    Types.LISTACCESS_,
                                    1,
                                 toLocaleString_native,
                                 Types.EXECUTE_)
                                ),)

toLocaleString_wrapper = Types.Function(('this',),
                                        toLocaleString_operations,
                                        static=False)
'''
toLocaleString function END
'''

'''
toPrecision function START
'''
def toPrecision_native(number,precision=None):
    if precision == None or precision == Types.undefined:
        return toLocaleString_native(number)
    precision = int(precision)
    if precision <= 0:
        raise Exception()#!!!!!!!!!!!!!!!!!!!!!!!!!!!

    precision -= 1 

    splitted = str(number).split('.')
    if precision+1<len(splitted[0]):
        return toExponential_native(number,precision)
    else:
        return toFixed_native(number,precision)

toPrecision_operations = (('return',
                            (
                                Types.VarName('precision'),
                                'value',
                                1,
                                Types.VarName('this'),
                                Types.LISTACCESS_,
                                 2,
                             toPrecision_native,
                             Types.EXECUTE_)
                            ),)

toPrecision_wrapper = Types.Function(('this','precision'),
                                  toPrecision_operations,
                                  static=False)
'''
toPrecision function END
'''

'''
toString function START
'''
def toString_native(x, base):
    if base == None or base == Types.undefined or base == 10:
        return toLocaleString_native(x)
    x = int(x)
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()
    return String.String.new((String.string_native(''.join(digits)),),{})

toString_operations = (('return',
                            (
                                Types.VarName('radix'),
                                'value',
                                1,
                                Types.VarName('this'),
                                Types.LISTACCESS_,
                                 2,
                             toString_native,
                             Types.EXECUTE_)
                            ),)

toString_wrapper = Types.Function(('this','radix'),
                                  toString_operations,
                                  static=False)
'''
toString function END
'''

'''
valueOf function START
'''
def valueOf_native(number_native):
    return Number.new((number_native,),{})

valueOf_operations = (('return',
                       ('value',
                        1,
                        Types.VarName('this'),
                        Types.LISTACCESS_,
                        1,
                        valueOf_native,Types.EXECUTE_)),)
valueOf_wrapper = Types.Function(('this',),
                                 valueOf_operations,
                                 static=False)
'''
valueOf function END
'''

Number.methods = {'toExponential':toExponential_wrapper,
                  'toFixed':toFixed_wrapper,
                  'toLocaleString':toLocaleString_wrapper,
                  'toPrecision':toPrecision_wrapper,
                  'toString':toString_wrapper,
                  'valueOf':valueOf_wrapper}







