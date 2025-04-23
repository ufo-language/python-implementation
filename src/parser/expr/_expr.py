from parser.prim.one_of import p_one_of

def p_expr(parse_call_record):
    return p_one_of((), parse_call_record)
