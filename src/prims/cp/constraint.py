from alltypes.expr.binop import BinOp
from alltypes.literal.primitive import Primitive
from prims.cp._system import CP_System

class Constraint (Primitive):
    
    """ Adds a constraint to a system. """
    
    def __init__(self):
        param_rules = (
            (Primitive.term_type('CP_System'), BinOp),
        )
        super().__init__('constraint', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        system = args[0]
        constraint = args[1]
        CP_System.add_constraint(system, constraint)
        return system
