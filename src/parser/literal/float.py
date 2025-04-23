from parser.prim.spot import p_spot

def p_float(parse_call_record):
    value = p_spot('Float', parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('Float', value[1])
    return value
