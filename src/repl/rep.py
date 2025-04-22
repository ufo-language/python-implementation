import parser.lexer
import parser.parser

def rep(input_string):
    print("rep '", input_string, "'", sep='')
    expr = _read(input_string)
    value = _eval(expr)
    _print(value)

def _read(input_string):
    tokens = parser.lexer.tokenize(input_string)
    expr = parser.parser.parse(tokens)
    return expr

def _eval(expr):
    pass

def _print(value):
    pass
