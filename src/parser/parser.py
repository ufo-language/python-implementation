class ParseCallRecord:

    __slots__ = ('parser_table', 'object_builder', 'tokens', 'token_index', 'memo_table', 'memo_key')

    def __init__(self, parser_table, object_builder, tokens):
        self.parser_table = parser_table
        self.object_builder = object_builder
        self.tokens = tokens
        self.token_index = 0
        self.memo_table = {}
        self.memo_key = None

def parse_entry_point(parser_name, parser_table, object_builder, tokens):
    parse_call_record = ParseCallRecord(parser_table, object_builder, tokens)
    return parse(parser_name, parse_call_record)

def parse(parser_name, parse_call_record):
    # check for memoized value
    memo_key = (parser_name, parse_call_record.token_index)
    memo_value = parse_call_record.memo_table.get(memo_key)
    if memo_value is not None:
        parse_value = memo_value[0]
        parse_call_record.token_index = memo_value[1]
        return parse_value
    # do the parse
    parser = parse_call_record.parser_table.get(parser_name)
    if parser is None:
        raise Exception(f"parser.parse did not find parser '{parser_name}'")
    # print(f"parser.parse trying {parser_name}/{parser}")
    saved_token_index = parse_call_record.token_index
    saved_memo_key = parse_call_record.memo_key
    parse_call_record.memo_key = memo_key
    parse_result = parser(parse_call_record)
    parse_call_record.memo_table[memo_key] = (parse_result, parse_call_record.token_index)
    # print(f"parser.parse {parser_name}/{parser} returning", parse_result)
    if parse_result is None:
        parse_call_record.token_index = saved_token_index
    parse_call_record.memo_key = saved_memo_key
    # save the memo
    return parse_result
