from parser.prim.spot import p_spot

def p_string(parse_call_record):
    value = p_spot('String', parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('String', value[1])
    return value
