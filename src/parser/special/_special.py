from parser.prim.ignore import ignore
from parser.prim.spot import p_spot_specific

def p_open_bracket(parse_call_record):
    return ignore(p_spot_specific('Special', '[', parse_call_record))

def p_close_bracket(parse_call_record):
    return ignore(p_spot_specific('Special', ']', parse_call_record))

def p_comma(parse_call_record):
    return ignore(p_spot_specific('Special', ',', parse_call_record))
