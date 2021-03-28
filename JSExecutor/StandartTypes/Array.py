from StandartTypes import String
from StandartTypes import Number
from StandartTypes import Boolean
from CodeStructures import Types


'''
Array constructor START
'''

def Array_constructor_native(args):
    to_return = []
    if len(args) == 0:
        return to_return
    elif len(args) == 1 and\
        str(args[0].typeof()) == 'number':
        if not args[0].is_int():
            raise Exception()#!!!!!!!!!!!!!!
        for i in range(int(args[0])):
            to_return.append(Types.undefined)
    else:
        to_return = list(args)
    return to_return


Array_METHODS = {}
Array_CONSTRUCTOR_OPERATIONS = (('var_change',
                      ('this.','value'),
                      (Types.VarName('arguments'),
                       1,
                       Array_constructor_native,
                       Types.EXECUTE_)),
                       ('return',('value',
                                  1,
                                  Types.VarName('this.'),
                                  Types.LISTACCESS_)),
                       )
Array_CONSTRUCTOR = Types.Function((),
                                   Array_CONSTRUCTOR_OPERATIONS,)

Array = Types.Class(String.String.new((String.string_native('object'),),{}),
                    Array_CONSTRUCTOR,
                    Array_METHODS)
'''
Array constrictor END
'''

'''
concat function START
'''
def concat_native(args):
    array = args[0]
    elements = args[1:]
    native_array = array['value']
    to_return = native_array.copy()
    for element in elements:
        value = element.this.get('value',[])
        if isinstance(value,list):
            for sub_element in value:
                to_return.append(sub_element)
        else:
            to_return.append(element)
    return Array.new(to_return,{})

concat_operations = (('return',
                      (Types.VarName('arguments'),
                       1,
                       concat_native,Types.EXECUTE_)),
                     )
concat_wrapper = Types.Function(('this','elements'),
                                concat_operations,
                                static=False)
Array_METHODS['concat'] = concat_wrapper
'''
concat function END
'''

'''
length function START

non standart function for array, if no arguments passed returns length of array
if passend number argument, sets new length for array, returns length of array
'''
def length_native(array,new_length):
    if new_length == Types.undefined:
        return Number.Number.new((len(array),),{})
    try:
        new_length_native = int(new_length)
        if new_length_native<0:
            raise Exception()
    except:
        raise Exception()#!!!!!!!!!!!!!!!
    
    if new_length_native > len(array):
        for i in range(new_length_native-len(array)):
            array.append(Types.undefined)
    elif new_length_native < len(array):
        for i in range(len(array)-new_length_native):
            array.pop()
    return new_length

length_operations = (('return',
                      (Types.VarName('new_length'),
                       'value',
                       1,
                       Types.VarName('this'),
                       Types.LISTACCESS_,
                       2,
                       length_native,Types.EXECUTE_)),)

length_wrapper = Types.Function(('this','new_length'),
                                length_operations,
                                static=False)
Array_METHODS['length'] = length_wrapper

'''
length function END
'''



'''
every function START
'''
every_loop_if_branches = (('if_condition',(Types.VarName('ret'),
                                           1,
                                           Types.VarName('Boolean'),
                                           Types.NEW_,
                                           Types.NOT_)),
                          ('return',(False,
                                     1,
                                     Types.VarName('Boolean'),
                                     Types.NEW_,))
                          )
every_loop_if = Types.If(every_loop_if_branches)

every_loop_condition = ((Types.VarName('this_array'),
                         0,
                         Types.ClassExecute('length'),Types.EXECUTE_),
                        Types.VarName('counter'),
                        Types.MORE_)
every_loop_operations = (('let','ret',
                          ('this.',
                           1,
                           Types.VarName('this'),
                           Types.LISTACCESS_,

                            Types.VarName('counter'),    
                                                       
                            Types.VarName('counter'),
                            'value',
                            2,
                            Types.VarName('this'),
                            Types.LISTACCESS_,

                           3,
                           Types.VarName('callback'),
                           Types.EXECUTE_)
                          ),
                         ('if',every_loop_if),
                         ('var_change',('counter',),(Types.VarName('counter'),
                                                  Number.Number.new((1,),{},),
                                                  Types.PLUS_))
                         )
every_loop = Types.Loop(every_loop_condition,
                        every_loop_operations)

every_operations = (('var','counter',(Number.Number.new((0,),{}),)),
                    ('var','this_array',('this.',
                                         1,
                                         Types.VarName('this'),
                                         Types.LISTACCESS_)),
                    ('loop',every_loop),
                    ('return',(True,
                               1,
                               Types.VarName('Boolean'),
                               Types.NEW_,))
                    )
every = Types.Function(('this','callback'),
                       every_operations,
                       static=False)

Array_METHODS['every'] = every
'''
every function END
'''

'''
push function START
'''
def push_native(args):
    array = args[0]
    elements = args[1:]
    array_native = array['value']
    for element in elements:
        array_native.append(element)
    return Number.Number.new((len(array_native),),
                             {})

push_operations = (('return',(Types.VarName('arguments'),
                              1,
                              push_native,
                              Types.EXECUTE_)),)

push_wrapper = Types.Function(('this','elements'),
                              push_operations,
                              static=False)
Array_METHODS['push'] = push_wrapper

'''
push function END
'''

'''
pop function START
'''
def pop_native(array):
    return array.pop()
pop_operations = (('return',('value',
                             1,
                             Types.VarName('this'),
                             Types.LISTACCESS_,

                             1,
                             pop_native,
                             Types.EXECUTE_)),)
pop_wrapper = Types.Function(('this',),
                             pop_operations,
                             static=False)
Array_METHODS['pop'] = pop_wrapper
'''
pop function END
'''

'''
shift function START
'''
def shift_native(array):
    return array.pop(0)

shift_operations = (('return',('value',
                               1,
                               Types.VarName('this'),
                               Types.LISTACCESS_,

                               1,
                             shift_native,
                             Types.EXECUTE_)),)
shift_wrapper = Types.Function(('this',),
                             shift_operations,
                             static=False)
Array_METHODS['shift'] = shift_wrapper
'''
shift function END
'''

'''
unshift function START
'''
def unshift_native(args):
    array = args[0]
    elements = args[1:]
    array_native = array['value']
    for element in elements:
        array_native.insert(0,element)
    return Number.Number.new((len(array_native),),
                             {})


unshift_operations = (('return',(Types.VarName('arguments'),
                                 1,
                                unshift_native,
                                Types.EXECUTE_)),)

unshift_wrapper = Types.Function(('this','elements'),
                              unshift_operations,
                              static=False)
Array_METHODS['unshift'] = unshift_wrapper
'''
unshift function END
'''


'''
filter function START
'''
filter_loop_if_branches = (('if_condition',(Types.VarName('ret'),
                                            1,
                                            Types.VarName('Boolean'),
                                            Types.NEW_)),
                          ('let','push_return',(Types.VarName('new_array'),

                                                Types.VarName('counter'),
                                                'value',
                                                2,
                                                Types.VarName('this'),
                                                Types.LISTACCESS_,

                                                1,
                                                Types.ClassExecute('push'),
                                                Types.EXECUTE_))
                          )
filter_loop_if = Types.If(filter_loop_if_branches)

filter_loop_condition = (Types.VarName('this_array'),
                          0,
                          Types.ClassExecute('length'),
                          Types.EXECUTE_,
                        Types.VarName('counter'),
                        Types.MORE_)
filter_loop_operations = (('let','ret',
                          (('this.',),Types.ListName('this'),
                              Types.VarName('counter'),

                               Types.VarName('counter'),
                               'value',
                               2,
                               Types.VarName('this'),
                               Types.LISTACCESS_,

                              3,
                           Types.VarName('callback'),
                           Types.EXECUTE_)
                          ),
                         ('if',filter_loop_if),
                         ('var_change',('counter',),(Types.VarName('counter'),
                                                  Number.Number.new((1,),{},),
                                                  Types.PLUS_))
                         )
filter_loop = Types.Loop(filter_loop_condition,
                        filter_loop_operations)

filter_operations = (('var','counter',(Number.Number.new((0,),{}),)),
                    ('var','this_array',('this.',
                                         1,
                                         Types.VarName('this'),
                                         Types.LISTACCESS_)),
                    ('var','new_array',(0,
                                        Types.VarName('Array'),
                                        Types.NEW_)),
                    ('loop',filter_loop),
                    ('return',(Types.VarName('new_array'),))
                    )
filter = Types.Function(('this','callback'),
                       filter_operations,
                       static=False)

Array_METHODS['filter'] = filter
'''
filter function END
'''


'''
forEach function START
'''
inloop_operations = ('let','new_length',(Types.VarName('new_array'),
                                         Types.VarName('ret'),
                                         1,
                                         Types.ClassExecute('push'),
                                         Types.EXECUTE_))

forEach_loop_condition = ((Types.VarName('this_array'),
                           0,
                           Types.ClassExecute('length'),
                           Types.EXECUTE_),
                        Types.VarName('counter'),
                        Types.MORE_)
forEach_loop_operations = (('let','ret',
                          ('this.',
                           1,
                           Types.VarName('this'),
                           Types.LISTACCESS_,

                              Types.VarName('counter'),

                               Types.VarName('counter'),
                               'value',
                               2,
                               Types.VarName('this'),
                               Types.LISTACCESS_,

                              3,
                           Types.VarName('callback'),
                           Types.EXECUTE_)
                          ),
                         inloop_operations,
                         ('var_change',('counter',),(Types.VarName('counter'),
                                                  Number.Number.new((1,),{},),
                                                  Types.PLUS_))
                         )
forEach_loop = Types.Loop(forEach_loop_condition,
                        forEach_loop_operations)

forEach_operations = (('var','counter',(Number.Number.new((0,),{}),)),
                    ('var','this_array',('this.',
                                         1,
                                         Types.VarName('this'),
                                         Types.LISTACCESS_)),
                    ('var','new_array',(0,
                                        Types.VarName('Array'),
                                        Types.NEW_)),
                    ('loop',forEach_loop),
                    ('return',(Types.VarName('new_array'),))
                    )
forEach = Types.Function(('this','callback'),
                       forEach_operations,
                       static=False)

Array_METHODS['forEach'] = forEach
'''
forEach function END
'''


'''
indexOf function START
'''
indexOf_loop_if_operations = (('if_condition',(Types.VarName('searchElement'),

                                                Types.VarName('counter'),
                                                'value',
                                                2,
                                                Types.VarName('this'),
                                                Types.LISTACCESS_,

                                               Types.STRICTEQUAL_)),
                              ('return',(Types.VarName('counter'),)))
indexOf_loop_if = Types.If(indexOf_loop_if_operations)

indexOf_loop_condition = ((Types.VarName('this_array'),
                           0,
                           Types.ClassExecute('length'),
                           Types.EXECUTE_),
                        Types.VarName('counter'),
                        Types.MORE_)
indexOf_loop_operations = (('if',indexOf_loop_if),
                         ('var_change',('counter',),(Types.VarName('counter'),
                                                  Number.Number.new((1,),{},),
                                                  Types.PLUS_))
                         )

indexOf_loop = Types.Loop(indexOf_loop_condition,
                        indexOf_loop_operations)

indexOf_operations = (('var','counter',(Number.Number.new((0,),{}),)),
                    ('var','this_array',('this.',
                                         1,
                                         Types.VarName('this'),
                                         Types.LISTACCESS_)),
                    ('loop',indexOf_loop),
                    ('return',(Number.Number.new((-1,),{}),))
                    )
indexOf = Types.Function(('this','searchElement'),
                       indexOf_operations,
                       static=False)
Array_METHODS['indexOf'] = indexOf
'''
indexOf function END
'''

'''
join function START
'''
join_loop_condition = (Types.VarName('length-1'),
                        Types.VarName('counter'),
                        Types.MORE_)
join_loop_operations = (('var','to_return',(Types.VarName('to_return'),

                                            Types.VarName('counter'),
                                            'value',
                                            2,
                                            Types.VarName('this'),
                                            Types.LISTACCESS_,

                                            1,
                                        Types.ClassExecute('concat'),
                                        Types.EXECUTE_),),
                        ('var','to_return',(Types.VarName('to_return'),
                                            Types.VarName('separator'),
                                            1,
                                      Types.ClassExecute('concat'),
                                      Types.EXECUTE_),),
                         ('var_change',('counter',),(Types.VarName('counter'),
                                                  Number.Number.new((1,),{}),
                                                  Types.PLUS_)),
                         )

join_loop = Types.Loop(join_loop_condition,
                        join_loop_operations)

if_branches = (('if_condition',(Types.VarName('this_array'),
                                0,
                                Types.ClassExecute('length'),
                                Types.EXECUTE_,
                                0,
                                1,
                                Types.VarName('Number'),
                                Types.NEW_,
                                Types.STRICTEQUAL_,
                                Types.NOT_)),
               ('var','to_return',(Types.VarName('to_return'),

                                    Types.VarName('counter'),
                                    'value',
                                    2,
                                    Types.VarName('this'),
                                    Types.LISTACCESS_,

                                   1,
                                      Types.ClassExecute('concat'),
                                      Types.EXECUTE_),)
               )

join_operations = (('var','counter',(0,
                                     1,
                                     Types.VarName('Number'),
                                     Types.NEW_)),
                    ('var','this_array',('this.',
                                         1,
                                         Types.VarName('this'),
                                         Types.LISTACCESS_)),
                    ('var','to_return',(String.String.new((String.string_native(''),),{}),)),
                    ('var','length-1',(Types.VarName('this_array'),
                                       0,
                                       Types.ClassExecute('length'),
                                       Types.EXECUTE_,
                                        Number.Number.new((1,),{}),
                                        Types.MINUS_,),),
                    ('loop',join_loop),
                    ('if',Types.If(if_branches)),
                    ('return',(Types.VarName('to_return'),))
                    )

default_values = {'separator':String.String.new((String.string_native(','),),{})}
join = Types.Function(('this','separator'),
                       join_operations,
                       default_values=default_values,
                       static=False)
Array_METHODS['join'] = join
'''
join function END
'''

'''
lastIndexOf function START
'''
lastIndexOf_loop_if_operations = (('if_condition',(Types.VarName('searchElement'),

                                                Types.VarName('counter'),
                                                'value',
                                                2,
                                                Types.VarName('this'),
                                                Types.LISTACCESS_,

                                               Types.STRICTEQUAL_)),
                              ('return',(Types.VarName('counter'),)))
lastIndexOf_loop_if = Types.If(lastIndexOf_loop_if_operations)

lastIndexOf_loop_condition = (-1,
                            Types.VarName('counter'),
                            Types.LESS_)
lastIndexOf_loop_operations = (('if',lastIndexOf_loop_if),
                         ('var_change',('counter',),(Types.VarName('counter'),
                                                  Number.Number.new((1,),{},),
                                                  Types.MINUS_))
                         )

lastIndexOf_loop = Types.Loop(lastIndexOf_loop_condition,
                        lastIndexOf_loop_operations)

def counter_native(array,fromIndex):
    if fromIndex == Types.undefined:
        length_number = array.execute_function('length',(),{})
        length_number.this['value'] -= 1
        return length_number
    fromIndex_native = int(fromIndex)
    length_number = array.execute_function('length',(),{})
    if fromIndex_native >= int(length_number):
        length_number.this['value'] -= 1
        return length_number
    if fromIndex_native<0:
        length_number.this['value'] += fromIndex_native
        return length_number
    return fromIndex


lastIndexOf_operations = (('var','counter',(Types.VarName('fromIndex'),

                                            'this.',
                                            1,
                                            Types.VarName('this'),
                                            Types.LISTACCESS_,

                                            2,
                                            counter_native,
                                            Types.EXECUTE_)),
                    ('var','this_array',('this.',
                                         1,
                                         Types.VarName('this'),
                                         Types.LISTACCESS_)),
                    ('loop',lastIndexOf_loop),
                    ('return',(Number.Number.new((-1,),{}),))
                    )
lastIndexOf = Types.Function(('this','searchElement','fromIndex'),
                       lastIndexOf_operations,
                       static=False)
Array_METHODS['lastIndexOf'] = lastIndexOf
'''
lastIndexOf function END
'''


'''
map function START
'''
Array_METHODS['map'] = forEach
'''
map function END
'''


'''
reduce function START
'''
reduce_loop_stop_condition = ('this.',
                              1,
                              Types.VarName('this'),
                              Types.LISTACCESS_,

                              0,
                              Types.ClassExecute('length'),
                              Types.EXECUTE_,
                              Types.VarName('counter'),
                              Types.MORE_)
reduce_loop_operations = (('let','b',(Types.VarName('counter'),
                                    'value',
                                    2,
                                    Types.VarName('this'),
                                    Types.LISTACCESS_,)),
                     ('let','a',(Types.VarName('result'),)),
                    ('var_change',('result',),(Types.VarName('b'),
                                            Types.VarName('a'),
                                            2,
                                            Types.VarName('callback'),
                                            Types.EXECUTE_)
                        ),
                    ('var_change',('counter',),(Types.VarName('counter'),
                                             Number.Number.new((1,),{}),
                                             Types.PLUS_))
                     )
reduce_loop = Types.Loop(reduce_loop_stop_condition,
                         reduce_loop_operations)


reduce_operations = (('let','counter',(Number.Number.new((1,),{}),)),
                     ('var','result',(Number.Number.new((0,),{}),
                                      'value',
                                      2,
                                      Types.VarName('this'),
                                      Types.LISTACCESS_)),
                     ('loop',reduce_loop),
                     ('return',(Types.VarName('result'),))
                    )
reduce = Types.Function(('this','callback'),
                        reduce_operations,
                        static=False)
Array_METHODS['reduce'] = reduce
'''
reduce function END
'''
