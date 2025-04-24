from parser.special._special import p_dollar
from parser.prim.list_of import p_list_of

def p_set(parse_call_record):
    if p_dollar(parse_call_record) is None:
        return None
    value = p_list_of('{', 'Any', ',', '}', parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('Set', value)
    return value
