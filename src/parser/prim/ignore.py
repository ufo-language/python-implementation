IGNORE_STRING = '%IGNORE%'

def ignore(parse_result):
    if parse_result is None:
        return None
    return IGNORE_STRING
