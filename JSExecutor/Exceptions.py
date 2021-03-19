
class ReferenceError(Exception):
    def __init__(self,var_name):
        self.var_name = var_name
        self.message = f'ReferenceError: {self.var_name} is not defined'
        super().__init__(self.message)


class KeyWordVarName(Exception):
    def __init__(self,key_word):
        self.key_word = key_word
        self.message = f'Key word "{self.key_word}" can\'t be a name for variable'
        super().__init__(self.message)

class BadVarName(Exception):
    def __init__(self,symbol):
        self.symbol = symbol
        self.message = f'Symbol {self.symbol} can\'t be in variable\'s name'
        super().__init__(self.message)

class EOF(Exception):
    def __init__(self,symbol):
        self.symbol = symbol
        self.message = f'Reached end of file, but didn\'t find {symbol}'
        super().__init__(self.message)

class BadSliceNumber(Exception):
    def __init__(self,number):
        self.number = number
        self.message = f'Expected 2 numbers for slice not {self.number}'
        super().__init__(self.message)

class BadListIndex(Exception):
    def __init__(self,data):
        self.data = data
        self.message = f'List indexes must be in type of {tuple} not {type(self.data)}'
        super().__init__(self.message)

class AttributeError(Exception):
    def __init__(self,mother_class:str,attribute):
        self.mother_class = mother_class
        self.attribute = attribute
        self.message = f'Object "{self.mother_class}" doesnt have attribute {self.attribute}'
        super().__init__(self.message)

class NotCallable(Exception):
    def __init__(self,obj):
        self.object = obj
        self.message = f'{self.object} is not callable'
        super().__init__(self.message)
