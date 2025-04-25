from alltypes.data.binding import Binding
from parser.prim.seq import p_seq

def p_binding(parse_call_record):
    parse_call_record.memo_table[parse_call_record.memo_key] = (None, -1)  # prevents unbounded recursion
    value = p_seq(('Any', Binding.CHAR, 'Any'), parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('Binding', value)
    return value
