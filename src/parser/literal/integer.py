from parser.prim.spot import p_spot

def p_integer(parse_call_record):
    value = p_spot('Integer', parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('Integer', value[1])
    return value
