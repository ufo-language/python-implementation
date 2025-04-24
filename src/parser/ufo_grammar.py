# expressions
from parser.expr._any import p_any
from parser.expr._expr import p_expr
from parser.expr.assign import p_assign
# data types
from parser.data._data import p_data
from parser.data.array import p_array
from parser.data.binding import p_binding
from parser.data.hashtable import p_hash_table
from parser.data.list import p_list
from parser.data.queue import p_queue
from parser.data.set import p_set
# literals
from parser.literal._literal import p_literal
from parser.literal.boolean import p_boolean
from parser.literal.float import p_float
from parser.literal.integer import p_integer
from parser.literal.nil import p_nil
from parser.literal.string import p_string
from parser.literal.symbol import p_symbol
# special
from parser.special._special import *

PARSER_TABLE = {
    # expressions
    'Any': p_any,
    'Expr': p_expr,
    'Assign': p_assign,
    # data types
    'Data': p_data,
    'Array': p_array,
    'Binding': p_binding,
    'HashTable': p_hash_table,
    'List': p_list,
    'Queue': p_queue,
    'Set': p_set,
    # literals
    'Literal': p_literal,
    'Boolean': p_boolean,
    'Float': p_float,
    'Integer': p_integer,
    'Nil': p_nil,
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
    '=': p_single_equal,
    '$': p_dollar,
    '#': p_hashmark,
    '~': p_tilde,
    ':=': p_colon_equal
}
