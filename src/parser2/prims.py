from parser2.parser import parse
from parser2.parse_exception import parse_exception
from parser2.parser_state import ParserState

IGNORE = '%IGNORE%'

def apply(fun, parser):
    def _parser(parser_state):
        if parse(parser, parser_state):
            parser_state.value = fun(parser_state.value)
            return True
        return False
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

debug_depth = 0

def indent():
    return '| ' * debug_depth

def debug(message, parser):
    def _parser(parser_state):
        global debug_depth

        if callable(parser):
            parser_name = parser.__qualname__
            # print(parser.__qualname__.split('.')[0])
        else:
            parser_name = parser

        # token = parser_state.next_token()
        tokens = [token[1] for token in parser_state.tokens[parser_state.index:]]
        if message:
            print(f"{indent()}debug {message} trying '{parser_name}' tokens={tokens}")
        else:
            print(f"{indent()}debug trying '{parser_name}' tokens={tokens}")

        debug_depth += 1
        success = parse(parser, parser_state)
        debug_depth -= 1

        if message:
            print(f"{indent()}debug {message} '{parser}' tokens={tokens} -> {success}, value={parser_state.value}")
        else:
            print(f"{indent()}debug '{parser}' tokens={tokens} -> {success}, value={parser_state.value}")
        return success

    return _parser

def fail(parser_state):
    return False

def ignore(parser):
    def _parser(parser_state):
        if parse(parser, parser_state):
            parser_state.value = IGNORE
            return True
        return False
    return _parser

def list_of(open, elem, sep, close, bar=None):
    def _proper_list(parser_state):
        parser = seq(open, sep_by(elem, sep), require(close))
        success = parse(parser, parser_state)
        return success
    def _improper_list(parser_state):
        parser = seq(open, maybe(seq(sep_by(elem, sep), one_of(seq(bar, elem), succeed(None)))), close)
        success = parse(parser, parser_state)
        return success
    return _proper_list if bar is None else _improper_list

def log(message, parser=None):
    def _parser(parser_state):
        print(message)
        parser_state.value = IGNORE
        return True
    return _parser

def many(parser, min=0):
    def _parser(parser_state):
        elems = []
        n = 0
        ctx = parser_state.get_ctx()
        while parse(parser, parser_state):
            elems.append(parser_state.value)
            n += 1
        if n < min:
            parser_state.set_ctx(ctx)
            return False
        parser_state.value = elems
        return True
    return _parser

def maybe(parser):
    def _parser(parser_state):
        success = parse(parser, parser_state)
        if not success:
            parser_state.value = IGNORE
        return True
    return _parser

def one_of(*parsers):
    '''
    Returns the most successful parse out of a number of parsers,
    where "most successful" = the longest parse.
    '''
    def _parser(parser_state):
        # keep track of the longest parse
        saved_results = []
        saved_parsers = []
        max_index_value = -1
        max_index_index = -1
        saved_ctx = parser_state.get_ctx()
        for parser in parsers:
            if parse(parser, parser_state):
                # remember this parse result
                if parser_state.index > max_index_value:
                    ctx = parser_state.get_ctx()
                    saved_results.append(ctx)
                    saved_parsers.append(parser)
                    max_index_value = parser_state.index
                    max_index_index = len(saved_results) - 1
            parser_state.set_ctx(saved_ctx)
        if max_index_value == -1:
            return False
        ctx = saved_results[max_index_index]
        parser_state.set_ctx(ctx)
        return True
    return _parser

def recursion_barrier(parser_state):
    parser_name = parser_state.current_parser_name
    memo_key = (parser_name, parser_state.index)
    # print(f"prev_rec2 {memo_key}")
    parser_state.memo_table[memo_key] = ((parser_state.index, None), False)  # prevent recursion
    # print(f"{indent()}prevent_recursion memo_table =", parser_state.memo_table)
    parser_state.value = IGNORE
    return True

def require(parser, parser_descriptor=None):
    def _parser(parser_state):
        if parse(parser, parser_state):
            return True
        parse_exception(f"Expected {parser if parser_descriptor is None else parser_descriptor}", parser_state)
    return _parser

# for the combinator version see 'succeed'
def returning(value, parser):
    def _parser(parser_state):
        if parse(parser, parser_state):
            parser_state.value = value
            return True
        return False
    return _parser

def sep_by(elem, sep):
    #return one_of(seq(elem, maybe(seq(sep, require(elem, f"{elem} after {sep}")))), succeed([]))
    def _parser(parser_state):
        success = parse(one_of(seq(recursion_barrier, elem, maybe(seq(sep, require(elem, f"{elem} after {sep}")))), succeed([])), parser_state)
        # the parser returns one of:
        # 1. the empty list []
        # 2. a single value
        # 3. a list of one or more values
        # so check for a single value here
        if not isinstance(parser_state.value, list):
            parser_state.value = [parser_state.value]
        return success
    return _parser

def seq(*parsers):
    def _parser(parser_state):
        saved_ctx = parser_state.get_ctx()
        results = []
        # print(f"{indent()}++ seq starting", parsers)
        for parser in parsers:
            # print(f"{indent()}++ seq trying", parser, "token=", parser_state.next_token())
            if parse(parser, parser_state):
                value = parser_state.value
                if value != IGNORE:
                    results.append(parser_state.value)
            else:
                # print(f"{indent()}++ seq", parser, "failed")
                parser_state.set_ctx(saved_ctx)
                return False
        if len(results) == 1:
            parser_state.value = results[0]
        else:
            parser_state.value = results
        return True
    return _parser

def show_tokens(parser_state):
    print("tokens:")
    for n in range(parser_state.index, len(parser_state.tokens)):
        token = parser_state.tokens[n]
        print(f"{n:3}. {token}")
    parser_state.value = IGNORE
    return True

def spot(expected_type, expected_value=None, strip=True):
    def _parser1(parser_state):
        token = parser_state.current_token()
        if token[0] == expected_type:
            parser_state.value = token
            if strip:
                parser_state.value = parser_state.value[1]
            parser_state.advance()
            return True
        return False
    def _parser2(parser_state):
        token = parser_state.current_token()
        if token[0] == expected_type:
            if token[1] == expected_value:
                parser_state.value = IGNORE
                parser_state.advance()
                return True
        return False
    return _parser1 if expected_value is None else _parser2

# Note that spot() now does a strip() by default
# def strip(parser):
#     def _parser(parser_state):
#         if parse(parser, parser_state):
#             parser_state.value = parser_state.value[1]
#             return True
#         return False
#     return _parser

# for the function version see 'returning'
def succeed(value):
    def _parser(parser_state):
        parser_state.value = value
        return True
    return _parser
