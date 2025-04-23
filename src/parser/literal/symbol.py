from parser.prim.spot import p_spot

def p_symbol(parse_call_record):
    value = p_spot('Symbol', parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('Symbol', value[1])
    return value
