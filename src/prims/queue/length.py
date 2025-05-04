from alltypes.data.queue import Queue
from alltypes.literal.integer import Integer
from alltypes.literal.primitive import Primitive

class Length (Primitive):
    
    """ Returns the length of a Queue. """
    
    def __init__(self):
        param_rules = (
            (Queue,),
        )
        super().__init__('length', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        q = args[0]
        n_elems = q.length()
        return Integer(n_elems)
