# From C++
# using ParserName = std::string;
# using Tokens = Object*;  // expected to be a UFO::Data::Array
# using TokenIndex = int;
# using ParseResult = std::optional<Object*>;
# using MemoKey = std::pair<ParserName, TokenIndex>;
# using MemoValue = std::pair<ParseResult, TokenIndex>;
# using MemoTable = std::unordered_map<MemoKey, MemoValue>;

# using ParseCallRecord = struct {
#     const Tokens& tokens;
#     TokenIndex& tokenIndex;
#     MemoTable& memoTable;
#     MemoKey memoKey;
# };

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
    parser = parse_call_record.parser_table.get(parser_name)
    if parser is None:
        raise Exception(f"parser.parse did not find parser '{parser_name}'")
    # print(f"parser.parse trying {parser_name}/{parser}")
    parse_result = parser(parse_call_record)
    # print(f"parser.parse {parser_name}/{parser} returning", parse_result)
    return parse_result
