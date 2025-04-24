from parser.prim.seq import p_seq

def p_if(parse_call_record):
    value = p_seq(('if', 'RequireAny', 'then', 'RequireAny', 'MaybeElseClause'), parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('If', value)
    return value
