# standard lexer actions

def ignore_char(lexer, char):
    pass

def keep_char(lexer, char):
    if char:
        lexer._word += char

def reuse_char(lexer, char):
    lexer._cs.unget()

# any character that's not an operator is a special character

def special_char(lexer, char):
    token = ('Special', char, lexer.get_saved_pos())
    lexer._tokens.append(token)
    lexer._word = ''

# lexer actions to create data types

def create_binary_int(lexer, char):
    token = ('Integer', int(lexer._word, 2), lexer.get_saved_pos())
    lexer._tokens.append(token)
    lexer._word = ''

def create_float(lexer, char):
    token = ('Float', float(lexer._word), lexer.get_saved_pos())
    lexer._tokens.append(token)
    lexer._word = ''

def create_hex_int(lexer, char):
    token = ('Integer', int(lexer._word, 16), lexer.get_saved_pos())
    lexer._tokens.append(token)
    lexer._word = ''

def create_int(lexer, char):
    token = ('Integer', int(lexer._word), lexer.get_saved_pos())
    lexer._tokens.append(token)
    lexer._word = ''

def create_oper(lexer, char):
    token = ('Operator', lexer._word, lexer.get_saved_pos())
    lexer._tokens.append(token)
    lexer._word = ''    

def create_string(lexer, char):
    token = ('String', lexer._word, lexer.get_saved_pos())
    lexer._tokens.append(token)
    lexer._word = ''

def create_symbol(lexer, char):
    token = ('Symbol', lexer._word, lexer.get_saved_pos())
    lexer._tokens.append(token)
    lexer._word = ''

def create_word(lexer, char):
    w = lexer._word
    # check for true and false first because 'true' and 'false'
    # are also in the list of reserved words
    if w == lexer._true:
        token = ('Boolean', True, lexer.get_saved_pos())
    elif w == lexer._false:
        token = ('Boolean', False, lexer.get_saved_pos())
    elif w in lexer._reserved_words:
        token = ('Reserved', lexer._word, lexer.get_saved_pos())
    else:
        token = ('Identifier', lexer._word, lexer.get_saved_pos())
    lexer._tokens.append(token)
    lexer._word = ''

# other actions

def eol(lexer, char):
    token = ('EOL', None, lexer.get_saved_pos())
    lexer._tokens.append(token)
    lexer._word = ''

def inject(char):
    def _inject(lexer, _):
        lexer._word += char
    return _inject

def save_pos(lexer, char):
    lexer.save_pos()
