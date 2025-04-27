from ufo_exception import UFOException

def parse_exception(message, parser_state):
    print("parse_exception called")
    raise UFOException(message, tokens=parser_state.tokens, index=parser_state.index, parser=parser_state.current_parser_name, prev_parser=parser_state.previous_parser_name)
