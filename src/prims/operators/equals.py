import sys

from alltypes.data.binding import Binding
from alltypes.literal.primitive import Primitive

class Equals (Primitive):
    
    def __init__(self):
        param_rules = (
            (object, object),
        )
        super().__init__('=', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        lhs = args[0]
        rhs = args[1]
        return Binding(lhs, rhs)
