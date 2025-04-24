from parser.prim.one_of import p_one_of

def p_data(parse_call_record):
    return p_one_of(('Array', 'List','Queue'), parse_call_record)
