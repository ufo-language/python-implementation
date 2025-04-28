import alltypes.literal.nil
from ufo_exception import UFOException
import lexer.ufo_syntax
import parser.ufo_grammar

def rep(input_string, etor):
    if len(input_string.strip()) == 0:
        return
    try:
        expr = _read(input_string)
        if expr is None:
            print("rep.rep() Parse error")
            return
        value = _eval(expr, etor)
        _print(value)
    except UFOException as exn:
        print(exn)

import lexer.ufo_syntax
import parser.ufo_grammar

def _read(input_string):
    # expr = parser.ufo_parser.parse_string(input_string)
    syntax = lexer.ufo_syntax.tokenize
    grammar = parser.ufo_grammar.ufo_parsers()
    expr = parser.parser.parse_string(input_string, syntax, grammar)
    return expr

def _eval(expr, etor):
    # print(f"rep._eval got expr {expr}")
    value = expr.eval(etor)
    # print(f"rep._eval({expr}) -> {value}")
    return value

def _print(value):
    if type(value) != alltypes.literal.nil.Nil:
        print(f"{value!r} :: {value.type_name()}")
