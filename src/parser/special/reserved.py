from parser.prim.ignore import ignore
from parser.prim.spot import p_spot_specific

def p_reserved_if(parse_call_record):
    return ignore(p_spot_specific('Reserved', 'if', parse_call_record))

def p_reserved_then(parse_call_record):
    return ignore(p_spot_specific('Reserved', 'then', parse_call_record))

def p_reserved_else(parse_call_record):
    return ignore(p_spot_specific('Reserved', 'else', parse_call_record))
