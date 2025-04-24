class ParseException (Exception):

    __slots__ = ('message', 'parse_call_record')

    def __init__(message, parse_call_record):
        self.message = message
        self.parse_call_record = parse_call_record

    def __repr__(self):
        return self.message
