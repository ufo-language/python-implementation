from parser.parse_exception import parse_exception
from parser.parser import parse
from parser.prim.sep_by import p_sep_by

def p_list_of(open, elem, sep, close, parse_call_record):
    if parse(open, parse_call_record) is None:
        return None
    elems = p_sep_by(elem, sep, parse_call_record)
    if parse(close, parse_call_record) is None:
        raise parse_exception(f"Parse exception: closing token '{close}' expected", parse_call_record)
    return elems
