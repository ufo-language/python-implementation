from parser.special._special import p_tilde
from parser.prim.list_of import p_list_of

def p_queue(parse_call_record):
    if p_tilde(parse_call_record) is None:
        return None
    value = p_list_of('[', 'Any', ',', ']', parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('Queue', value)
    return value
