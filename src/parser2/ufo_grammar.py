from parser2.prims import *

from alltypes.expr.identifier import Identifier
from alltypes.data.array import Array
from alltypes.data.binding import Binding
from alltypes.data.list import List
from alltypes.literal.boolean import Boolean
from alltypes.literal.integer import Integer
from alltypes.literal.float import Float
from alltypes.literal.nil import Nil
from alltypes.literal.string import String
from alltypes.literal.symbol import Symbol

def ufo_parsers():
    return {
        'Any': one_of('Expression', 'Data', 'Literal', 'Nil'),
        # expression
        'Expression': one_of('Identifier'),
        'Identifier': apply(Identifier, strip(spot('Identifier'))),
        # data
        'Data'      : one_of('Array', 'Binding', 'HashTable', 'List', 'Queue', 'Set'),
        'Array'     : apply(Array.from_parser, list_of('{', 'Any', ',', '}')),
        'Binding'   : apply(Binding.from_parser, seq(recursion_barrier, 'Any', ':', 'Any')),
        'HashTable' : fail,
        'List'      : apply(List.from_parser, list_of('[', 'Any', ',', ']', '|')),
        'Queue'     : fail,
        'Set'       : fail,
        # literal
        'Literal'   : one_of('Boolean', 'Float', 'Integer', 'String', 'Symbol'),
        'Boolean'   : apply(Boolean, strip(spot('Boolean'))),
        'Integer'   : apply(Integer, strip(spot('Integer'))),
        'Float'     : apply(Float, strip(spot('Float'))),
        'Nil'       : apply(Nil, strip(spot('Reserved', 'nil'))),
        'String'    : apply(String, strip(spot('String'))),
        'Symbol'    : apply(Symbol, strip(spot('Symbol'))),
        # special
        '['         : ignore(spot('Special', '[')),
        ']'         : ignore(spot('Special', ']')),
        '{'         : ignore(spot('Special', '{')),
        '}'         : ignore(spot('Special', '}')),
        '('         : ignore(spot('Special', '(')),
        ')'         : ignore(spot('Special', ')')),
        ':'         : ignore(spot('Operator', ':')),
        ','         : ignore(spot('Special', ',')),
        '|'         : ignore(spot('Special', '|'))
    }
