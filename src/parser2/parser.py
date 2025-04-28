from parser2.parser_state import ParserState

IGNORE = '%IGNORE%'

def parse_string(input_string, syntax, grammar):
    tokens = syntax(input_string)
    parser_state = ParserState(grammar, None, tokens)
    success = parse('Program', parser_state)
    return parser_state.value if success else None

def _spot_lexeme(lexeme, parser_state):
    token = parser_state.next_token()
    if token[1] == lexeme:
        parser_state.value = lexeme
        parser_state.advance()
        parser_state.value = IGNORE
        return True
    return False

depth = 0
def parse(parser, parser_state):
    global depth
    depth += 1
    #assert depth < 40
    if callable(parser):
        depth -= 1
        return parser(parser_state)
    if isinstance(parser, str):
        parser_state.previous_parser_name = parser_state.current_parser_name
        parser_state.current_parser_name = parser
        # check memo table
        memo_key = (parser, parser_state.index)
        memo_value = parser_state.memo_table.get(memo_key)
        if memo_value is not None:
            (ctx, success) = memo_value
            parser_state.set_ctx(ctx)
            depth -= 1
            return success
        # call the parser function
        parser_state.memo_key = memo_key
        parser_function = parser_state.parser_table.get(parser)
        if parser_function is None:
            success = _spot_lexeme(parser, parser_state)
        else:
            success = parser_function(parser_state)
        # store result in memo table
        ctx = parser_state.get_ctx()
        parser_state.memo_table[memo_key] = (ctx, success)
        depth -= 1
        return success
    raise Exception(f"parser.parse got unknown parser type {parser} :: {type(parser)}")

