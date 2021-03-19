import Exceptions
import Types


skip_symbols = ('\n','\r',' ')
cant_be_in_name = '[]{}\\|/?.,<>+()*&^%$#@!\'":`~ '
reserved_words = {'a':('await',),

                  'b':('break',),

                  'c':('case','catch','class',
                       'const','continue'),

                  'd':('debugger','default','delete',
                        'do'),

                  'e':('else','enum','export',
                       'extends'),

                  'f':('false','finally','for',
                       'function'),
                  
                  
                  'i':('if','import','in',
                       'instanceof'),

                  'l':('let',),

                  'n':('new','null'),

                  'r':('return',),

                  's':('static','super','switch'),

                  't':('this','throw','true',
                       'try','typeof'),

                  'v':('var','void'),

                  'w':('while','with'),
                   }


def parse_right_side(right_side:str,global_vars:dict):

    


def parse_var(script:str,start:int,global_vars:dict):
    last_equal = False
    line_end = start

    '''
    Searches for the last '=' sign and ';' 

    last_equal = False/int
    line_end = int - index of end of instruction 
    '''
    while script[line_end] != ';':       
        if script[line_end] == '=':
            last_equal = line_end
        elif script[line_end] == '"':
            line_end = script.find('"',line_end+1)
            if line_end == -1:
                raise Exceptions.EOF('"')
        elif script[line_end] == '\'':
            line_end = script.find('\'',line_end+1)
            if line_end == -1:
                raise Exceptions.EOF('\'')
        line_end += 1


    if last_equal != False:
        left_side = script[start:last_equal].split('=')
    else:
        left_side = [script[start:line_end]]

    #gets parsed left side
    counter = 0
    while counter<len(left_side):
        left_side[counter] = left_side[counter].strip(' \n\r')
        for character in left_side[counter]:
            if character in cant_be_in_name:
                raise Exceptions.BadVarName(character)
        words = reserved_words.get(left_side[counter],())
        if left_side[counter][0] in words:
            raise Exceptions.KeyWordVarName(left_side[counter])
        counter += 1

    if last_equal == False: #if one var is undefined
        global_vars[left_side[0]] = Types.undefined
        return line_end+1
    last_equal += 1

    '''
    right side of line
    '''
    right_side = script[last_equal:line_end]




    






def parse_script(global_vars:dict,script:str):
    start = 0
    while start < len(script):       
        symbol = script[start]
        if symbol in skip_symbols:
            start += 1
            continue

        command = ''

        words = reserved_words.get(symbol,False)
        if words != False:
            for word in words:
                if script[start:start+len(word)] == word:
                    command = word
                    break

        if command == 'var':
            start += 3
            start = parse_var(script,start,global_vars)


if __name__ == '__main__':
    parse_script({},'var    a     =    9;')

