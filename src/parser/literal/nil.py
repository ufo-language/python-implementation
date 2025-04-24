from parser.prim.spot import p_spot_specific

def p_nil(parse_call_record):
    value = p_spot_specific('Reserved', 'nil', parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('Nil', None)
    return value
