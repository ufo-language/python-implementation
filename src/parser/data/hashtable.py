from parser.special._special import p_hashmark
from parser.prim.list_of import p_list_of

def p_hash_table(parse_call_record):
    if p_hashmark(parse_call_record) is None:
        return None
    value = p_list_of('{', 'Binding', ',', '}', parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('HashTable', value)
    return value
