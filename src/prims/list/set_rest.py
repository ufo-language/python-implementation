from alltypes.data.list import List
from alltypes.literal.primitive import Primitive

class SetRest (Primitive):
    
    """ Sets the rest of a List. """
    
    def __init__(self):
        param_rules = (
            (List, object),
        )
        super().__init__('set_rest', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        lst = args[0]
        rest = args[1]
        lst.set_rest(rest)
        return lst
