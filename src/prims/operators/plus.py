import sys

from alltypes.literal.integer import Integer
from alltypes.literal.real import Real
from alltypes.literal.string import String
from alltypes.literal.symbol import Symbol
from alltypes.literal.primitive import Primitive
from ufo_exception import UFOException

class Plus (Primitive):
    
    """ Returns the arithmetic sum of two numeric values, or joins a value to a String. """

    def __init__(self):
        param_rules = (
            ((Integer, Real), (Integer, Real)),
            (String, object),
            ((Integer, Real),)
        )
        super().__init__('+', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        match (param_rule_num):
            case 0:
                lhs = args[0]
                rhs = args[1]
                if type(lhs) is Symbol or type(rhs) is Symbol:
                    return self.handle_infinity(lhs, rhs)
                lhs = lhs._value
                rhs = rhs._value
                return Integer(lhs + rhs)
            case 1:
                lhs = args[0]._value
                s = lhs + str(args[1])
                return String(s)
            case 2:
                rhs = args[0]
                return rhs
        raise SystemError(f"Unhandled case {param_rule_num}")
