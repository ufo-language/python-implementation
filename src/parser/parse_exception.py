from ufo_exception import UFOException

def parse_exception(message, parse_call_record):
    raise UFOException(message, tokens=parse_call_record.tokens, token_index=parse_call_record.token_index)
