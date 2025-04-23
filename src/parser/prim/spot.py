def p_spot(type_name, parse_call_record):
    token = parse_call_record.tokens[parse_call_record.token_index]
    if token[0] == type_name:
        parse_call_record.token_index += 1
        return token
    return None

def p_spot_specific(type_name, value, parse_call_record):
    token = parse_call_record.tokens[parse_call_record.token_index]
    if token[0] == type_name:
        if token[1] == value:
            parse_call_record.token_index += 1
            return token
    return None
