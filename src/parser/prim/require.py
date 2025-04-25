import parser.parser
from parser.parse_exception import parse_exception

def require(parser_name):
    def parse_fun(parse_call_record):
        value = parser.parser.parse(parser_name, parse_call_record)
        if value is None:
            raise parse_exception(f"Expected '{parser_name}'", parse_call_record)
    return parse_fun
