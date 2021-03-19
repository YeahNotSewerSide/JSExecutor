
#import inspect
from StandartTypes import Number
from StandartTypes import String
from StandartTypes import Boolean
from StandartTypes import Array
from CodeStructures import Types

if __name__ == '__main__':
    GLOBAL_PARAMETERS = {'Number':Number.Number,
                         'Boolean':Boolean.Boolean,
                         'String':String.String,
                         'Array':Array.Array}
    print('Testing Number:')

    number = Number.Number.new(('77',),GLOBAL_PARAMETERS)
    print('Initial value:',number)

    exp_number = number.execute_function('toExponential',(4,),GLOBAL_PARAMETERS)
    print('toExponential:',exp_number)

    fixed_number = number.execute_function('toFixed',(2,),GLOBAL_PARAMETERS)
    print('toFixed:',fixed_number)
    
    string_number = number.execute_function('toLocaleString',tuple(),GLOBAL_PARAMETERS)
    print('toLocaleString:',string_number)

    precision_number = number.execute_function('toPrecision',tuple(),GLOBAL_PARAMETERS)
    print('toPrecision:',precision_number)

    tostring_number = number.execute_function('toString',(10,),GLOBAL_PARAMETERS)
    print('toString:',tostring_number)

    valueof_number = number.execute_function('valueOf',(),GLOBAL_PARAMETERS)
    print('valueOf:',valueof_number)

    print()

    print('Testing Boolean:')
 
    boolean = Boolean.Boolean.new((number,),GLOBAL_PARAMETERS)
    print('Initial value:',boolean)
    
    tostring_boolean = boolean.execute_function('toString',(),GLOBAL_PARAMETERS)
    print('toString:',tostring_boolean)

    valueof_boolean = boolean.execute_function('valueOf',(),GLOBAL_PARAMETERS)
    print('valueOf:',valueof_boolean)

    print()
    
    print('Testing String:')
    
    index = Number.Number.new(('1',),GLOBAL_PARAMETERS)

    string = String.String.new((String.string_native('string'),),GLOBAL_PARAMETERS)
    print('Initial value:',string)

    charat_string = string.execute_function('charAt',(index,),GLOBAL_PARAMETERS)
    print('charAt:',charat_string)

    charcodeat_string = string.execute_function('charCodeAt',(index,),GLOBAL_PARAMETERS)
    print('charCodeAt:',charcodeat_string)

    concat_string = string.execute_function('concat',(index,index),GLOBAL_PARAMETERS)
    print('concat:',concat_string)

    index = Number.Number.new(('3',),GLOBAL_PARAMETERS)
    substring = String.String.new((String.string_native('i'),),GLOBAL_PARAMETERS)
    indexof_string = string.execute_function('indexOf',(substring,index),GLOBAL_PARAMETERS)
    print('indexOf:',indexof_string)
    
    lastindexof_string = string.execute_function('lastIndexOf',(substring,),GLOBAL_PARAMETERS)
    print('lastIndexOf:',lastindexof_string)

    substring = String.String.new((String.string_native('a'),),GLOBAL_PARAMETERS)
    localecompare_string = string.execute_function('localeCompare',
                                                   (substring,),
                                                   GLOBAL_PARAMETERS)
    print('localeCompare:',localecompare_string)

    length_string = string.get_attribute('length')
    print('length:',length_string)





    print()
    
    print('Testing Array:')

    number = Number.Number.new((4,),GLOBAL_PARAMETERS)
    array = Array.Array.new((number,number),
                            GLOBAL_PARAMETERS)
    print('Array:',array)

    concat_array = array.execute_function('concat',
                                          (array,array),
                                          GLOBAL_PARAMETERS)
    print('concat:',concat_array)

    length_array = array.execute_function('length',(Number.Number.new((2,),GLOBAL_PARAMETERS),),GLOBAL_PARAMETERS)
    print('length:',length_array)

    test_callback = Types.Function(('element','index','array'),
                                   (('return',((True,),Types.ClassNew('Boolean'))),))
    every_array = array.execute_function('every',(test_callback,),GLOBAL_PARAMETERS)
    print('every:',every_array)

    push_array = array.execute_function('push',(length_array,length_array),GLOBAL_PARAMETERS)
    print('push:',push_array)

    pop_array = array.execute_function('pop',(),GLOBAL_PARAMETERS)
    print('pop:',pop_array)

    shift_array = array.execute_function('shift',(),GLOBAL_PARAMETERS)
    print('shift:',shift_array)

    unshift_array = array.execute_function('unshift',(length_array,length_array,),GLOBAL_PARAMETERS)
    print('unshift:',unshift_array)

    if_callback = Types.If((('if_condition',(Types.VarName('element'),
                                             Number.Number.new((3,),{}),
                                             Types.LESS_)),
                            ('return',(Boolean.Boolean.new((True,),{}),)),
                            ('if_condition',(True,)),
                            ('return',(Boolean.Boolean.new((False,),{}),))
                            ))
    test_callback = Types.Function(('element','index','array'),
                                   (('if',if_callback),))
    filter_array = array.execute_function('filter',(test_callback,),GLOBAL_PARAMETERS)
    print(filter_array)

    string_new = String.String.new((String.string_native('string'),),GLOBAL_PARAMETERS)
    push_array = array.execute_function('push',(string,),GLOBAL_PARAMETERS)
    print('push:',push_array)
    indexof_array = array.execute_function('indexOf',(string_new,),GLOBAL_PARAMETERS),
    print('indexOf:',indexof_array)

    string_new = String.String.new((String.string_native(' , '),),GLOBAL_PARAMETERS)
    join_array = array.execute_function('join',(),GLOBAL_PARAMETERS)
    print('join:',join_array)

    string_new = String.String.new((String.string_native('string'),),GLOBAL_PARAMETERS)
    push_array = array.execute_function('push',(string,),GLOBAL_PARAMETERS)
    print('push:',push_array)
    start_index = Number.Number.new((500,),GLOBAL_PARAMETERS)
    lastindexof_array = array.execute_function('lastIndexOf',(string_new,start_index),GLOBAL_PARAMETERS),
    print('lastIndexOf:',lastindexof_array)

    callback = Types.Function(('a','b'),
                              (('return',(Types.VarName('a'),
                                         Types.VarName('b'),
                                         Types.PLUS_)),))
    reduce_array = array.execute_function('reduce',(callback,),GLOBAL_PARAMETERS)
    print('reduce:',reduce_array)
