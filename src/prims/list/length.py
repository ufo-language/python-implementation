from alltypes.data.list import List
from alltypes.literal.integer import Integer
from alltypes.literal.primitive import Primitive

class Length (Primitive):
    
    """ Returns the length of a List. """
    
    def __init__(self):
        param_rules = (
            (List,),
        )
        super().__init__('length', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        lst = args[0]
        n_elems = lst.length()
        return Integer(n_elems)
