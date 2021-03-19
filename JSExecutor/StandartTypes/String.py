# -*- coding: utf-8 -*-

from CodeStructures import Types
from StandartTypes import Number
import inspect


'''
String constructor START
'''
def length_native(string):
    return Number.Number.new((len(string),),
                             {})
STRING_CONSTRUCTOR_OPERATIONS = (('var_change',
                                  ('this.','value'),
                                  (Types.VarName('input'),(),
                                   Types.ClassExecute('toString'),
                                   Types.EXECUTE_)),
                                 ('var_change',
                                  ('this.','length'),
                                  (((('value',),Types.ListName('this.')),),
                                   length_native,Types.EXECUTE_)),
                                 ('return',(('value',),Types.ListName('this.')))
                                 )
STRING_CONSTRUCTOR_WRAPPER = Types.Function(('input',),
                                            STRING_CONSTRUCTOR_OPERATIONS,
                                            static=False)
'''
String constructor END
'''


'''
charCodeAt function START
'''
def charCodeAt_native(string,index):
    if index == Types.undefined:
        index = 0
    index = int(index)
    if index > len(string)-1:
        return Types.NaN
    return Number.Number.new((ord(string[index]),),
                             {})

charCodeAt_operations = (('return',
                      ((
                         (('value',),Types.ListName('this'))
                        ,(Types.VarName('index'),),),charCodeAt_native,Types.EXECUTE_)),)
charCodeAt = Types.Function(('this','index'),
                            charCodeAt_operations,
                            static=False)
'''
charCodeAt function END
'''


'''
String definition START
'''
STRING_CONSTRUCTOR_METHODS = {'charAt':None,
                              'charCodeAt':charCodeAt,
                              'concat':None,
                              'indexOf':None,
                              'toString':None,
                              }

String = Types.Class('string',
                     STRING_CONSTRUCTOR_WRAPPER,
                     STRING_CONSTRUCTOR_METHODS)
'''
String definition END
'''


'''
native string wrapper START
'''
string_native_methods = None
class string_native:
    def __init__(self,input:str):
        self.value = str(input)
    def __str__(self):
        return self.value
    def __repr__(self):
        return self.__str__()
    def toString(self):
        return str(self)
    def __getitem__(self,index):
        return String.new(string_native(self.value[index]))
    def execute_function(self,\
                        function_name:str,\
                        arguments:tuple,\
                        global_variables:dict):
        global string_native_methods
        return string_native_methods[function_name](self)
string_native_methods = dict(inspect.getmembers(string_native, predicate=inspect.isfunction))


def wrap_native_string(input:str):
    return string_native(input)
'''
native string wrapper END
'''



'''
charAt function START
'''
def charAt_native(string,index):
    if index == Types.undefined:
        index = 0
    index = int(index)
    if index > len(string)-1:
        return String.new((string_native(''),),
                          {})
    return String.new((string_native(string[index]),),
                      {})

charAt_operations = (('return',
                      ((
                         (('value',),Types.ListName('this'))
                        ,(Types.VarName('index'),),),charAt_native,Types.EXECUTE_)),)

charAt = Types.Function(('this','index'),
                        charAt_operations,
                        static=False
                        )
STRING_CONSTRUCTOR_METHODS['charAt'] = charAt

'''
charAt function END
'''


'''
concat function START
'''
def concat_native(original_string,*elements):
    to_return = original_string['value']
    for argument in elements:
        to_return = to_return + str(argument.execute_function('toString',
                                                                (),
                                                                {}))
    return String.new((wrap_native_string(to_return),),
                      {})

concat_operations = (('return',
                      (Types.VarName('arguments'),concat_native,Types.EXECUTE_)),
                     )

concat_wrapper = Types.Function(('this','elements'),
                                concat_operations,
                                static=False
                                )
STRING_CONSTRUCTOR_METHODS['concat'] = concat_wrapper
'''
concat function END
'''

'''
toString function START
'''
toString_operations = (('return',(('this.',),Types.ListName('this'))),
                     )
toString = Types.Function(('this',),
                                  toString_operations,
                                  static=False)
STRING_CONSTRUCTOR_METHODS['toString'] = toString

'''
toString function END
'''



'''
indexOf function START
'''
def indexOf_native(original_string:str,searchValue,fromIndex=0):
    if searchValue == Types.undefined:
        return -1
    if fromIndex == Types.undefined:
        fromIndex = 0
    searchValue_native = str(searchValue.execute_function('toString',
                                                      (),
                                                      {}))
    return Number.Number.new((original_string.find(searchValue_native,
                                                   int(fromIndex)),),
                             {})

indexOf_operations = (('return',
                      ((
                         (('value',),Types.ListName('this'))
                        ,(Types.VarName('searchValue'),),
                        (Types.VarName('fromIndex'),)),
                       indexOf_native,Types.EXECUTE_)),
                     )
indexOf_wrapper = Types.Function(('this','searchValue','fromIndex'),
                                 indexOf_operations,
                                 static=False)
STRING_CONSTRUCTOR_METHODS['indexOf'] = indexOf_wrapper   
'''
indexOf function END
'''


'''
lastIndexOf function START
'''
def lastIndexOf_native(original_string:str,searchValue,fromIndex=0):
    if searchValue == Types.undefined:
        return -1
    if fromIndex == Types.undefined:
        fromIndex = 0
    searchValue_native = str(searchValue.execute_function('toString',
                                                      (),
                                                      {}))
    return Number.Number.new((original_string.rfind(searchValue_native,
                                                   int(fromIndex)),),
                             {})

lastIndexOf_operations = (('return',
                      ((
                         (('value',),Types.ListName('this'))
                        ,(Types.VarName('searchValue'),),
                        (Types.VarName('fromIndex'),)),
                       lastIndexOf_native,Types.EXECUTE_)),
                     )
lastIndexOf_wrapper = Types.Function(('this','searchValue','fromIndex'),
                                 lastIndexOf_operations,
                                 static=False)
STRING_CONSTRUCTOR_METHODS['lastIndexOf'] = lastIndexOf_wrapper   
'''
lastIndexOf function END
'''

'''
localeCompare function START
'''

def localeCompare_native(string1,string2):
    string2_native_utf8 = str(string2.execute_function('toString',
                                                      (),
                                                      {}))
    string1_native_utf8 = string1
    
    if len(string1)>len(string2_native_utf8):
        for index,char in enumerate(string2_native_utf8):
            num_char_string1 = ord(string1_native_utf8[index])
            num_char_string2 = ord(char)
            if num_char_string1 < num_char_string2:
                return Number.Number.new((-1,),{})
            elif num_char_string1 > num_char_string2:
                return Number.Number.new((1,),{})
    else:
        for index,char in enumerate(string1_native_utf8):
            num_char_string2 = ord(string2_native_utf8[index])
            num_char_string1 = ord(char)
            if num_char_string1 < num_char_string2:
                return Number.Number.new((-1,),{})
            elif num_char_string1 > num_char_string2:
                return Number.Number.new((1,),{})
    return Number.Number.new((0,),{})

localeCompare_operations = (('return',
                      ((
                         (('value',),Types.ListName('this'))
                        ,(Types.VarName('param'),),),
                       localeCompare_native,Types.EXECUTE_)),
                     )

localeCompare_wrapper = Types.Function(('this','param'),
                                      localeCompare_operations,
                                      static=False)
STRING_CONSTRUCTOR_METHODS['localeCompare'] = localeCompare_wrapper 
'''
localeCompare function END
'''






