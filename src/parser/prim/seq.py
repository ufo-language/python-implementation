import parser.prim.ignore

def p_seq(parser_names, parse_call_record):
    saved_index = parse_call_record.token_index
    parse_results = []
    for parser_name in parser_names:
        parse_result = parser.parser.parse(parser_name, parse_call_record)
        if parse_result is None:
            parse_call_record.token_index = saved_index
            return None
        if parse_result is not parser.prim.ignore.IGNORE_STRING:
            parse_results.append(parse_result)
    if len(parse_results) == 1:
        return parse_results[0]
    return parse_results
