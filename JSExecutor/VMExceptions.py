class WrongCountOfArguments(Exception):
    def __init__(self):
        self.message = 'Count of arguments for function must be int type'
        super().__init__(self.message)
