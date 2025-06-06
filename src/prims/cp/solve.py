from alltypes.data.term import Term
from alltypes.literal.nil import Nil
from alltypes.literal.primitive import Primitive
from prims.cp._solve import CP_Solve

class Solve (Primitive):
    
    """ Solves a constraint system. """
    
    def __init__(self):
        param_rules = (
            (Term,),
        )
        super().__init__('solve', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        system = args[0]
        return CP_Solve.solve(system)
