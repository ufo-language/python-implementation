from alltypes.data.term import Term
from alltypes.expr.binop import BinOp
from alltypes.literal.primitive import Primitive
from prims.cp._support import CP_Constraint

class Constraint (Primitive):
    
    def __init__(self):
        param_rules = (
            (Term, BinOp),
        )
        super().__init__('constraint', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        variable = args[0]
        constraint = args[1]
        return CP_Constraint.add_to_var(constraint, variable)
