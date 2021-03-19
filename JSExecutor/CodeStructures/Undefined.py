class Undefined:
    def __init__(self):
        pass
    def __str__(self):
        return 'undefined'
    def __repr__(self):
        return 'undefined'
    def __bool__(self):
        return False
    def typeof(self):
        return 'undefined'
