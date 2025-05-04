from alltypes.data.list import List
from alltypes.literal.primitive import Primitive

class First (Primitive):
    
    """ Returns the first element of a List. """
    
    def __init__(self):
        param_rules = (
            (List,),
        )
        super().__init__('first', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        lst = args[0]
        return lst.first()
