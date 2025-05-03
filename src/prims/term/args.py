from alltypes.data.term import Term
from alltypes.literal.primitive import Primitive

class Args (Primitive):
    
    """ Returns a term's argument data structure. """
    
    def __init__(self):
        param_rules = (
            (Term,),
        )
        super().__init__('args', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        term = args[0]
        return term.args()
