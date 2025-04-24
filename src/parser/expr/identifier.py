from parser.prim.spot import p_spot

def p_identifier(parse_call_record):
    value = p_spot('Identifier', parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('Identifier', value[1])
    return value
