from alltypes.literal.primitive import Primitive
from alltypes.data.term import Term
from alltypes.object_construct import object_construct

class Construct (Primitive):
    
    def __init__(self):
        param_rules = (
            (Term,),
        )
        super().__init__('construct', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        return object_construct(args[0])
