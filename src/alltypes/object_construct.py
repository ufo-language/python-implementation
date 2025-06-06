from alltypes.expr.if_then import IfThen

def object_construct(term):
    term_name = term.name().name()
    if term_name == IfThen.type_name(None):
        return IfThen.construct_from_term(term)
    raise SystemError(f"construct is not implemented for type {term_name}")
