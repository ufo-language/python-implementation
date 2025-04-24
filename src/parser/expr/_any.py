from parser.prim.one_of import p_one_of

def p_any(parse_call_record):
    return p_one_of(('Expr', 'Data', 'Literal'), parse_call_record)

def p_require_any(parse_call_record):
    value = p_any(parse_call_record)
    if value is None:
        raise ParseException(f"Expected '{parser_name}'", parse_call_record)
    return value
