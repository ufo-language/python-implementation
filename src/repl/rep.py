import alltypes.literal.nil
from etor.ufo_exception import UFOException
import lexer.ufo_syntax
import parser.ufo_parser

def rep(input_string, etor):
    if len(input_string.strip()) == 0:
        return
    expr = _read(input_string)
    if expr is None:
        print("rep.rep() Parse error")
        return
    try:
        value = _eval(expr, etor)
        _print(value)
    except UFOException as exn:
        print(exn)

def _read(input_string):
    expr = parser.ufo_parser.parse_string(input_string)
    return expr

def _eval(expr, etor):
    # print(f"rep._eval got expr {expr}")
    value = expr.eval(etor)
    # print(f"rep._eval({expr}) -> {value}")
    return value

def _print(value):
    if type(value) != alltypes.literal.nil.Nil:
        print(value, '::', value.type_name())
