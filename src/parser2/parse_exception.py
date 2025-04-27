from ufo_exception import UFOException

def parse_exception(message, parser_state):
    raise UFOException(message, tokens=parser_state.tokens, index=parser_state.index)
