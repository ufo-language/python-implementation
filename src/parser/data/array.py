from parser.prim.list_of import p_list_of

def p_array(parse_call_record):
    value = p_list_of('{', 'Any', ',', '}', parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('Array', value)
    return value
