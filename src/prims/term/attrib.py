from alltypes.data.term import Term
from alltypes.literal.primitive import Primitive

class Attrib (Primitive):
    
    """ Returns a term's attribute. """
    
    def __init__(self):
        param_rules = (
            (Term,),
        )
        super().__init__('attrib', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        term = args[0]
        return term.attrib()
