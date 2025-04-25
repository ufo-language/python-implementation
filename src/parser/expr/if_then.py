from parser.parse_exception import parse_exception
import parser.parser
from parser.prim.seq import p_seq
import parser.prim.ignore

def p_if(parse_call_record):
    value = p_seq(('if', 'RequireAny', 'then', 'RequireAny', 'MaybeElse'), parse_call_record)
    if value is not None:
        value = parse_call_record.object_builder('If', *value)
    return value

def p_maybe_else(parse_call_record):
    if parser.parser.parse('else', parse_call_record) is None:
        return parser.prim.ignore.IGNORE_STRING
    value = parser.parser.parse('Any', parse_call_record)
    if value is None:
        raise parse_exception("Expression 'Any' expected after 'else'", parse_call_record)
    return value
