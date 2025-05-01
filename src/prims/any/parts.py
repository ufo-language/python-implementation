from alltypes.literal.primitive import Primitive

class Parts (Primitive):
    
    def __init__(self):
        param_rules = (
            (object,),
        )
        super().__init__('parts', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        return args[0].parts()
