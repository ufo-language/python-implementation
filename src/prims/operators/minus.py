import sys

from alltypes.literal.integer import Integer
from alltypes.literal.real import Real
from alltypes.literal.string import String
from alltypes.literal.symbol import Symbol
from alltypes.literal.primitive import Primitive
from prims.operators._inf import *
from ufo_exception import UFOException

class Minus (Primitive):
    
    """ Returns the arithmetic sum of two numeric values, or joins a value to a String. """

    def __init__(self):
        param_rules = (
            ((Integer, Real, Symbol), (Integer, Real, Symbol)),
            ((Integer, Real, Symbol),)
        )
        super().__init__('-', param_rules)

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
                rhs = args[0]
                if rhs is INF:
                    return MINUS_INF
                if rhs is PLUS_INF:
                    return MINUS_INF
                if rhs is MINUS_INF:
                    return PLUS_INF
                if type(rhs) == Integer:
                    return Integer(-rhs.value())
                if type(rhs) == Real:
                    return Real(-rhs.value())
                raise UFOException("Prefix operator does not handle argument", prefix_op=self, argument=rhs)
        raise SystemError(f"Unhandled case {param_rule_num}")

    def handle_infinity(self, lhs, rhs):
        if lhs is PLUS_INF:
            if rhs is MINUS_INF:
                return PLUS_INF
            if rhs is PLUS_INF:
                return UNDEFINED
            return lhs
        if lhs is MINUS_INF:
            if rhs is PLUS_INF:
                return MINUS_INF
            if rhs is MINUS_INF:
                return UNDEFINED
            return MINUS_INF
        if rhs is PLUS_INF:
            return MINUS_INF
        if rhs is MINUS_INF:
            return PLUS_INF
