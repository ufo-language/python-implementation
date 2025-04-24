# expressions
from parser.expr._any import p_any
from parser.expr._expr import p_expr
# data types
from parser.data._data import p_data
from parser.data.array import p_array
from parser.data.list import p_list
from parser.data.queue import p_queue
# literals
from parser.literal._literal import p_literal
from parser.literal.float import p_float
from parser.literal.integer import p_integer
from parser.literal.string import p_string
from parser.literal.symbol import p_symbol
# special
from parser.special._special import *

PARSER_TABLE = {
    # expressions
    'Any': p_any,
    'Expr': p_expr,
    # data types
    'Data': p_data,
    'Array': p_array,
    'List': p_list,
    'Queue': p_queue,
    # literals
    'Literal': p_literal,
    'Float': p_float,
    'Integer': p_integer,
    'String': p_string,
    'Symbol': p_symbol,
    # special
    '{': p_open_brace,
    '}': p_close_brace,
    '[': p_open_bracket,
    ']': p_close_bracket,
    # '(': p_open_paren,
    # ')': p_close_paren
    ',': p_comma,
    '~': p_tilde
}
