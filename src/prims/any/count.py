from alltypes.literal.integer import Integer
from alltypes.literal.primitive import Primitive
from alltypes.literal.symbol import Symbol

class Count (Primitive):
    
    """ Evaluates an expression. """
    
    def __init__(self):
        param_rules = (
            (object,),
        )
        super().__init__('count', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        count = args[0].count()
        if type(count) is Symbol:
            return count
        return Integer(count)
