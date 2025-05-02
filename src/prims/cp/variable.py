from alltypes.data.term import Term
from alltypes.expr.identifier import Identifier
from alltypes.literal.primitive import Primitive
from prims.cp._support import CP_Variable

class Variable (Primitive):
    
    def __init__(self):
        param_rules = (
            (Term, Identifier),
        )
        super().__init__('variable', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        return CP_Variable.create(args)
