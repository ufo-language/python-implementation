import sys

from alltypes.literal.integer import Integer
from alltypes.literal.real import Real
from alltypes.literal.string import String
from alltypes.literal.primitive import Primitive

class Plus (Primitive):
    
    def __init__(self):
        param_rules = (
            ((Integer, Real), (Integer, Real)),
            (String, object)
        )
        super().__init__('+', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        match (param_rule_num):
            case 0:
                lhs = args[0]._value
                rhs = args[1]._value
                return Integer(lhs + rhs)
            case 1:
                lhs = args[0]._value
                s = lhs + str(args[1])
                return String(s)
            case _:
                raise SystemError(f"Unhandled case {param_rule_num}")
