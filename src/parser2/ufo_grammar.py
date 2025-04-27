from parser2.prims import *

from alltypes.data.array import Array
from alltypes.data.binding import Binding
from alltypes.data.hashtable import HashTable
from alltypes.data.list import List
from alltypes.data.queue import Queue
from alltypes.data.set import Set

from alltypes.expr.identifier import Identifier
from alltypes.expr.if_then import IfThen

from alltypes.literal.boolean import Boolean
from alltypes.literal.integer import Integer
from alltypes.literal.float import Float
from alltypes.literal.nil import Nil
from alltypes.literal.string import String
from alltypes.literal.symbol import Symbol

def ufo_parsers():
    return {
        'Program'   : seq('Any', '!EOI'),
        '!EOI'      : require(ignore(spot('EOI')), 'End of input'),
        'Any'       : one_of('Expression', 'Data', 'Literal', 'Nil'),
        '!Any'      : require('Any'),
        # expression
        'Expression': one_of('Identifier', 'If'),
        'Identifier': apply(Identifier, strip(spot('Identifier'))),
        'If'        : apply(IfThen.from_parser, seq('if', '!Any', '!then', '!Any', maybe(seq('else', '!Any')))),
        # data
        'Data'      : one_of('Array', 'Binding', 'HashTable', 'List', 'Queue', 'Set'),
        'Array'     : apply(Array.from_parser, list_of('{', 'Any', ',', '}')),
        'Binding'   : apply(Binding.from_parser, seq(recursion_barrier, 'Any', ':', 'Any')),
        'HashTable' : apply(HashTable.from_parser, seq('#', list_of('{', 'Binding', ',', '}'))),
        'List'      : apply(List.from_parser, list_of('[', 'Any', ',', ']', '|')),
        'Queue'     : apply(Queue.from_parser, seq('~', list_of('[', 'Any', ',', ']'))),
        'Set'       : apply(Set.from_parser, seq('$', list_of('{', 'Any', ',', '}'))),
        # literal
        'Literal'   : one_of('Boolean', 'Float', 'Integer', 'String', 'Symbol'),
        'Boolean'   : apply(Boolean, strip(spot('Boolean'))),
        'Integer'   : apply(Integer, strip(spot('Integer'))),
        'Float'     : apply(Float, strip(spot('Float'))),
        'Nil'       : apply(Nil, strip(spot('Reserved', 'nil'))),
        'String'    : apply(String, strip(spot('String'))),
        'Symbol'    : apply(Symbol, strip(spot('Symbol'))),
        # reserved words
        'else'      : ignore(spot('Reserved', 'else')),
        'if'        : ignore(spot('Reserved', 'if')),
        'then'      : ignore(spot('Reserved', 'then')),
        '!then'     : require('then'),
        # special
        '['         : ignore(spot('Special', '[')),
        ']'         : ignore(spot('Special', ']')),
        '{'         : ignore(spot('Special', '{')),
        '}'         : ignore(spot('Special', '}')),
        '('         : ignore(spot('Special', '(')),
        ')'         : ignore(spot('Special', ')')),
        ':'         : ignore(spot('Operator', ':')),
        ','         : ignore(spot('Special', ',')),
        '|'         : ignore(spot('Special', '|')),
        '#'         : ignore(spot('Special', '#')),
        '~'         : ignore(spot('Special', '~')),
        '$'         : ignore(spot('Special', '$')),
    }
