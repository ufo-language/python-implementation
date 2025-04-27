from parser2.parser_state import ParserState

def parse_string(input_string, syntax, grammar):
    # print("parser2.parse input_string =", input_string)
    # tokens = lexer.ufo_syntax.tokenize(input_string)
    tokens = syntax(input_string)
    # print("parser2.parse tokens =", tokens)
    #  def __init__(self, parser_table, object_builder, tokens):
    # parser_state = ParserState(ufo_parsers(), None, tokens)
    parser_state = ParserState(grammar, None, tokens)
    success = parse('Any', parser_state)
    if success:
        value = parser_state.value
        # print(f"parser2.parse value = {value}, next token = {parser_state.next_token()}")
    else:
        # print(f"parser2.parse failed")
        value = None
    return value

depth = 0
def parse(parser, parser_state):
    global depth
    # print(f"{indent()}parse trying {parser}, next token={parser_state.next_token()}")
    depth += 1
    assert depth < 20
    if callable(parser):
        depth -= 1
        return parser(parser_state)
    if isinstance(parser, str):
        parser_state.most_recent_parser_name = parser
        # check memo table
        memo_key = (parser, parser_state.index)
        memo_value = parser_state.memo_table.get(memo_key)
        if memo_value is not None:
            (ctx, success) = memo_value
            parser_state.set_ctx(ctx)
            depth -= 1
            # print(f"{indent()}parse {parser} returning memoized value {memo_key} -> {memo_value}")
            return success
        # call the parser function
        # parser_state.memo_table[memo_key] = ((parser_state.index, None), False)  # should prevent recursion
        parser_state.memo_key = memo_key
        parser_function = parser_state.parser_table[parser]
        success = parser_function(parser_state)
        # store result in memo table
        ctx = parser_state.get_ctx()
        parser_state.memo_table[memo_key] = (ctx, success)
        # print(f"memoized {memo_key} = {ctx}")
        depth -= 1
        # if success:
        #     print(f"{indent()}parse {parser} returning {success} : {parser_state.value}")
        # else:
        #     print(f"{indent()}parse {parser} returning {success}")
        return success
    raise Exception(f"parser.parse got unknown parser type {parser} :: {type(parser)}")

