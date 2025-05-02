from alltypes.data.term import Term
from alltypes.literal.nil import Nil
from alltypes.literal.primitive import Primitive

class Solve (Primitive):
    
    """ Solves a constraint system. """
    
    def __init__(self):
        param_rules = (
            (Term,),
        )
        super().__init__('solve', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        system = args[0]
        print("Solve got system", system)
        return Nil()
