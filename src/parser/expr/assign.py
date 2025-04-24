from parser.prim.seq import p_seq

def p_assign(parse_call_record):
    parse_call_record.memo_table[parse_call_record.memo_key] = (None, -1)  # prevents unbounded recursion
    value = p_seq(('Any', ':=', 'Any'), parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('Assign', value)
    return value
