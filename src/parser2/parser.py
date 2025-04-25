from alltypes.literal.boolean import Boolean
from alltypes.literal.integer import Integer
from alltypes.literal.float import Float
from alltypes.literal.nil import Nil
from alltypes.literal.string import String
from alltypes.literal.symbol import Symbol

import lexer.ufo_syntax

class ParserState:

    __slots__ = (
        'parser_table', 'object_builder', 'tokens', 'index', 'value',
        'memo_table', 'memo_key', 'saved_ctx'
    )

    def __init__(self, parser_table, object_builder, tokens):
        self.parser_table = parser_table
        self.object_builder = object_builder
        self.tokens = tokens
        self.index = 0
        self.value = None
        self.memo_table = {}
        self.memo_key = None
        self.saved_ctx = []

    def current_token(self):
        return self.tokens[self.index]

    def advance(self, n=1):
        self.index += n

    def apply(self, fun):
        self.value = fun(self.value)

    def get_ctx(self):
        return (self.index, self.value)

    def set_ctx(self, ctx):
        (self.index, self.value) = ctx


def spot(expected_type, expected_value=None):
    def _parser1(parser_state):
        token = parser_state.current_token()
        if token[0] == expected_type:
            parser_state.value = token
            parser_state.advance()
            return True
        return False
    def _parser2(parser_state):
        token = parser_state.current_token()
        if token[0] == expected_type:
            if token[1] == expected_value:
                parser_state.value = token
                parser_state.advance()
                return True
        return False
    return _parser1 if expected_value is None else _parser2

def strip(parser_state):
    parser_state.apply(lambda value: value[1])
    return True

def one_of(*parsers):
    def _parser(parser_state):
        for parser in parsers:
            if parse(parser, parser_state):
                return True
        return False
    return _parser

def seq(*parsers):
    def _parser(parser_state):
        saved_ctx = parser_state.get_ctx()
        results = []
        for parser in parsers:
            if parse(parser, parser_state):
                value = parser_state.value
                if value != '%IGNORE%':
                    results.append(parser_state.value)
            else:
                parser_state.set_ctx(saved_ctx)
                return False
        if len(results) == 1:
            parser_state.value = results[0]
        else:
            parser_state.value = results
        return True
    return _parser

def compose(*parsers):
    def _parser(parser_state):
        saved_ctx = parser_state.get_ctx()
        for parser in parsers:
            if not parse(parser, parser_state):
                parser_state.set_ctx(saved_ctx)
                return False
        return True
    return _parser

def apply(fun):
    def _parser(parser_state):
        parser_state.value = fun(parser_state.value)
        return True
    return _parser

def parse(parser, parser_state):
    if callable(parser):
        return parser(parser_state)
    if isinstance(parser, str):
        parser_function = parser_state.parser_table[parser]
        return parser_function(parser_state)
    assert False

def parsers():
    return {
        'Any': one_of('Expression', 'Data', 'Literal', 'Nil'),
        # expression
        'Expression': one_of(),
        # data
        'Data': one_of(),
        # literal
        'Literal': one_of('Boolean', 'Float', 'Integer', 'String', 'Symbol'),
        'Boolean': compose(spot('Boolean'), strip, apply(Boolean)),
        'Integer': compose(spot('Integer'), strip, apply(Integer)),
        'Float': compose(spot('Float'), strip, apply(Float)),
        'Nil': compose(spot('Reserved', 'nil'), strip, apply(Nil)),
        'String': compose(spot('String'), strip, apply(String)),
        'Symbol': compose(spot('Symbol'), strip, apply(Symbol))
    }

#============================================================================

def parse_string(input_string):
    print("parser2.parse input_string =", input_string)
    tokens = lexer.ufo_syntax.tokenize(input_string)
    print("parser2.parse tokens =", tokens)
    #  def __init__(self, parser_table, object_builder, tokens):
    parser_state = ParserState(parsers(), None, tokens)
    success = parse('Any', parser_state)
    value = parser_state.value
    return value

