from parser.prim.one_of import p_one_of

def p_literal(parse_call_record):
    return p_one_of(('Float', 'Integer', 'String', 'Symbol'), parse_call_record)
