from alltypes.data.queue import Queue
from alltypes.literal.primitive import Primitive

class Deq (Primitive):
    
    """ Enqueues a value in a Queue. """
    
    def __init__(self):
        param_rules = (
            (Queue,),
        )
        super().__init__('deq', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        q = args[0]
        return q.deq()
