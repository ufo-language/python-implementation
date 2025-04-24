from parser.prim.one_of import p_one_of

def p_expr(parse_call_record):
    value = p_one_of(('Assign', 'Identifier', 'If'), parse_call_record)
    return value
