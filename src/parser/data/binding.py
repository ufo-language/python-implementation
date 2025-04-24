from parser.prim.seq import p_seq

def p_binding(parse_call_record):
    value = p_seq(('Any', '=', 'Any'), parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('Binding', value)
    return value
