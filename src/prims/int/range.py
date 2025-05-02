from alltypes.data.range import Range
from alltypes.literal.integer import Integer
from alltypes.literal.primitive import Primitive

class Int_Range (Primitive):
    
    """ Creates a Range. """
    
    def __init__(self):
        param_rules = (
            (Integer,),
            (Integer, Integer),
            (Integer, Integer, Integer)
        )
        super().__init__('range', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        from_value = 0
        to_value = 0
        by_value = Integer(1)
        match param_rule_num:
            case 0:
                to_value = args[0]
            case 1:
                from_value = args[0]
                to_value = args[1]
            case 2:
                from_value = args[0]
                to_value = args[1]
                by_value = args[2]
            case _:
                raise SystemError(f"Unhandled case {param_rule_num}")
        return Range(from_value, to_value, by_value)
