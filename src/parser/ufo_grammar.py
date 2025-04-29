from parser.prims import *

from alltypes.data.array import Array
from alltypes.data.binding import Binding
from alltypes.data.hashtable import HashTable
from alltypes.data.list import List
from alltypes.data.queue import Queue
from alltypes.data.set import Set

from alltypes.expr.apply import Apply
from alltypes.expr.assign import Assign
from alltypes.expr.function import Function
from alltypes.expr.identifier import Identifier
from alltypes.expr.if_then import IfThen
from alltypes.expr.seq import Seq

from alltypes.literal.boolean import Boolean
from alltypes.literal.integer import Integer
from alltypes.literal.float import Float
from alltypes.literal.nil import Nil
from alltypes.literal.string import String
from alltypes.literal.symbol import Symbol

def ufo_parsers():
    return {
        'Program'     : seq('Any', '!EOI'),
        '!EOI'        : require('EOI', 'End-of-Input'),
        'Any'         : one_of('Expression', 'Data', 'Literal'),
        '!Any'        : require('Any'),

        'Expression'  : one_of('Apply', 'Assign', 'Function', 'Identifier', 'If', 'Seq'),
        'Apply'       : apply(Apply.from_parser, seq(recursion_barrier, 'Any', 'ArgList')),
        'ArgList'     : list_of('(', 'Any', ',', ')'),
        'Assign'      : apply(Assign.from_parser, seq(recursion_barrier, 'Any', ':=', '!Any')),
        'Function'    : apply(Function.from_parser, seq('fun', one_of('Identifier', succeed(None)), sep_by('FunctionRule', '|'))),
        'FunctionRule': seq('ParamList', '=', 'Any'),
        'ParamList'   : list_of('(', 'Any', ',', ')'),
        'Identifier'  : apply(Identifier, spot('Identifier')),
        'If'          : apply(IfThen.from_parser, seq('if', '!Any', '!then', '!Any', maybe(seq('else', '!Any')))),
        '!then'       : require('then'),
        'Seq'         : apply(Seq.from_parser, list_of('(', 'Any', ';', ')')),

        'Data'        : one_of('Array', 'Binding', 'HashTable', 'List', 'Queue', 'Set'),
        'Array'       : apply(Array.from_parser, list_of('{', 'Any', ',', '}')),
        'Binding'     : apply(Binding.from_parser, seq(recursion_barrier, 'Any', ':', 'Any')),
        'HashTable'   : apply(HashTable.from_parser, seq('#', list_of('{', 'Binding', ',', '}'))),
        'List'        : apply(List.from_parser, list_of('[', 'Any', ',', ']', '|')),
        'Queue'       : apply(Queue.from_parser, seq('~', list_of('[', 'Any', ',', ']'))),
        'Set'         : apply(Set.from_parser, seq('$', list_of('{', 'Any', ',', '}'))),

        'Literal'     : one_of('Boolean', 'Float', 'Integer', 'Nil', 'String', 'Symbol'),
        'Boolean'     : apply(Boolean, one_of(returning(True, 'true'), returning(False, 'false'))),
        'Integer'     : apply(Integer, spot('Integer')),
        'Float'       : apply(Float, spot('Float')),
        'Nil'         : returning(Nil(), 'nil'),
        'String'      : apply(String, spot('String')),
        'Symbol'      : apply(Symbol, spot('Symbol')),
    }
