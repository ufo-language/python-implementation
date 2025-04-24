from parser.prim.ignore import ignore
from parser.prim.spot import p_spot_specific

def p_open_brace(parse_call_record):
    return ignore(p_spot_specific('Special', '{', parse_call_record))

def p_close_brace(parse_call_record):
    return ignore(p_spot_specific('Special', '}', parse_call_record))

def p_open_bracket(parse_call_record):
    return ignore(p_spot_specific('Special', '[', parse_call_record))

def p_close_bracket(parse_call_record):
    return ignore(p_spot_specific('Special', ']', parse_call_record))

def p_comma(parse_call_record):
    return ignore(p_spot_specific('Special', ',', parse_call_record))

def p_dollar(parse_call_record):
    return ignore(p_spot_specific('Special', '$', parse_call_record))

def p_single_equal(parse_call_record):
    return ignore(p_spot_specific('Operator', '=', parse_call_record))

def p_hashmark(parse_call_record):
    return ignore(p_spot_specific('Special', '#', parse_call_record))

def p_tilde(parse_call_record):
    return ignore(p_spot_specific('Special', '~', parse_call_record))
