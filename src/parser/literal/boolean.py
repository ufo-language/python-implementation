from parser.prim.spot import p_spot

def p_boolean(parse_call_record):
    value = p_spot('Boolean', parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('Boolean', value[1])
    return value
