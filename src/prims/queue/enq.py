from alltypes.data.queue import Queue
from alltypes.literal.primitive import Primitive

class Enq (Primitive):
    
    """ Enqueues a value in a Queue. """
    
    def __init__(self):
        param_rules = (
            (Queue, object),
        )
        super().__init__('enq', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        q = args[0]
        elem = args[1]
        q.enq(elem)
        return q
