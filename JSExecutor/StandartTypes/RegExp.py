from StandartTypes import String
from CodeStructures import Types


'''
RegExp constructor START
'''
RegExp_CONSTRUCTOR_OPERATIONS = (('var_change',
                                  ('this.','value'),
                                  (((Types.VarName('input'),),),Types.ClassExecute('toString'))))
RegExp_CONSTRUCTOR = Types.Function(('input',),
                        RegExp_CONSTRUCTOR_OPERATIONS,
                        static=False)
'''
RegExp constructor END
'''

'''
RegExp class definition START
'''
RegExp_METHODS = {}
RegExp = Types.Class(None,
                     RegExp_CONSTRUCTOR,
                     RegExp_METHODS)
RegExp.name = String.String.new((String.string_native('object'),),{})
'''
RegExp class definition END
'''


