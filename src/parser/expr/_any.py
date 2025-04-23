from parser.prim.one_of import p_one_of

def p_any(parse_call_record):
    return p_one_of(('Expr', 'Data', 'Literal'), parse_call_record)
