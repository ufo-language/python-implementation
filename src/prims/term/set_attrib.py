from alltypes.data.term import Term
from alltypes.literal.primitive import Primitive

class SetAttrib (Primitive):
    
    """ Sets a term's attribute. """
    
    def __init__(self):
        param_rules = (
            (Term, object),
        )
        super().__init__('set_attrib', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        term = args[0]
        value = args[1]
        term.set_attrib(value)
        return term
