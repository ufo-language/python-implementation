from parser.parse_exception import parse_exception
from parser.parser import parse

def p_sep_by(elem, sep, parse_call_record):
    elems = []
    first_iter = True
    while True:
        elem_res = parse(elem, parse_call_record)
        if elem_res is None:
            if first_iter:
                break
            raise parse_exception(f"p_sep_by expected elem '{elem}' after separator '{sep}'", parse_call_record)
        elems.append(elem_res)
        sep_res = parse(sep, parse_call_record)
        if sep_res is None:
            break
        first_iter = False
    return elems
