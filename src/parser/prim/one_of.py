import parser.parser

def p_one_of(parser_names, parse_call_record):
    ''' Returns the "most successful" (longest parse) of a number of parsers. '''
    saved_token_index = parse_call_record.token_index
    n_parsers = len(parser_names)
    # succeed on the longest successful parse
    saved_results = [None] * n_parsers
    max_token_index_value = -1
    max_token_index_index = -1
    # try each parser
    for n in range(n_parsers):
        parser_name = parser_names[n]
        # print(f"p_one_of {parser_names} trying {parser_name}")
        result = parser.parser.parse(parser_name, parse_call_record)
        # print(f"p_one_of {parser_names} : {parser_name} = {result}")
        saved_results[n] = result
        if result is not None:
            # record the longest parse
            if parse_call_record.token_index > max_token_index_value:
                max_token_index_value = parse_call_record.token_index
                max_token_index_index = n
        parse_call_record.token_index = saved_token_index
    if max_token_index_value > -1:
        # return the result of the longest parse
        parse_call_record.token_index = max_token_index_value
        # print(f"p_one_of {parser_names} returning", saved_results[max_token_index_index])
        return saved_results[max_token_index_index]
    # print(f"p_one_of {parser_names} returning None")
    return None
