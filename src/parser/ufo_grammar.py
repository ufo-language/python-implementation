from parser.prims import *

from alltypes.data.array import Array
# from alltypes.data.binding import Binding
from alltypes.data.hashtable import HashTable
from alltypes.data.list import List
from alltypes.data.queue import Queue
from alltypes.data.set import Set
from alltypes.data.term import Term

from alltypes.expr.apply import Apply
from alltypes.expr.assign import Assign
from alltypes.expr.binop import BinOp
from alltypes.expr.function import Function
from alltypes.expr.identifier import Identifier
from alltypes.expr.if_then import IfThen
from alltypes.expr.prefixop import PrefixOp
from alltypes.expr.quote import Quote
from alltypes.expr.scope_resolution import ScopeResolution
from alltypes.expr.seq import Seq
from alltypes.expr.subscript import Subscript

from alltypes.literal.boolean import Boolean
from alltypes.literal.integer import Integer
from alltypes.literal.nil import Nil
from alltypes.literal.real import Real
from alltypes.literal.string import String
from alltypes.literal.symbol import Symbol

from lexer.lexer import Lexer

def ufo_parsers():
    return {
        'Program'     : seq('Any', '!EOI'),
        '!EOI'        : require(Lexer.EOI, 'End-of-Input'),
        '!Any'        : require('Any'),

        'Any'         : one_of('Apply', 'Assign', 'BinOp', 'Function', 'If', 'PrefixOp', 'Quote', 'ScopeRes', 'Subscript', 'Data'),
        'Apply'       : apply(Apply.from_parser, seq(recursion_barrier, 'Any', 'ArgList')),
        'ArgList'     : list_of('(', 'Any', ',', ')'),
        'Assign'      : apply(Assign.from_parser, seq('Data', ':=', '!Any')),
        'BinOp'       : apply(BinOp.from_parser, seq(recursion_barrier, 'Any', 'Operator', '!Any')),
        'Operator'    : apply(Identifier, spot('Operator')),
        'Function'    : apply(Function.from_parser, seq(one_of('fun', 'macro'), one_of('Identifier', succeed(None)), sep_by('FunctionRule', '|'))),
        'fun'         : returning(False, spot('Reserved', 'fun')),
        'macro'       : returning(True, spot('Reserved', 'macro')),
        'FunctionRule': seq('ParamList', '=', 'Any'),
        'ParamList'   : list_of('(', 'Any', ',', ')'),
        'If'          : apply(IfThen.from_parser, seq('if', '!Any', '!then', '!Any', maybe(seq('else', '!Any')))),
        '!then'       : require('then'),
        'PrefixOp'    : apply(PrefixOp.from_parser, seq('Operator', 'Any')),
        'Quote'       : apply(Quote, seq('\'', 'Any', '\'')),
        'ScopeRes'    : apply(ScopeResolution.from_parser, sep_by('Identifier', ':', 2)),
        'Subscript'   : apply(Subscript.from_parser, seq(recursion_barrier, 'Any', '[', 'Any', ']')),

        'Data'        : one_of('Array', 'HashTable', 'List', 'Queue', 'Set', 'Term', 'Literal'),
        'Array'       : apply(Array.from_parser, list_of('{', 'Any', ',', '}')),
        # 'Binding'     : apply(Binding.from_parser, seq(recursion_barrier, 'Any', '=', 'Any')),
        'HashTable'   : apply(HashTable.ProtoHash.from_parser, seq('#', list_of('{', 'Any', ',', '}'))),
        'List'        : apply(List.from_parser, list_of('[', 'Any', ',', ']', '|')),
        'Queue'       : apply(Queue.from_parser, seq('~', list_of('[', 'Any', ',', ']'))),
        'Set'         : apply(Set.from_parser, seq('$', list_of('{', 'Any', ',', '}'))),
        'Term'        : apply(Term.from_parser, seq(recursion_barrier, 'Any', 'Array')),

        'Literal'     : one_of('Boolean', 'Real', 'Identifier', 'Integer', 'Nil', 'Seq', 'String', 'Symbol'),
        'Boolean'     : apply(Boolean, one_of(returning(True, 'true'), returning(False, 'false'))),
        'Integer'     : apply(Integer, spot('Integer')),
        'Real'        : apply(Real, spot('Real')),
        'Nil'         : returning(Nil(), 'nil'),
        'String'      : apply(String, spot('String')),
        'Symbol'      : apply(Symbol, spot('Symbol')),
        # these are not literals, but they parsed as literals:
        'Identifier'  : apply(Identifier, spot('Identifier')),
        'Seq'         : apply(Seq.from_parser, list_of('(', 'Any', ';', ')')),
    }
