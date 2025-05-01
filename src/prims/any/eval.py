from alltypes.literal.primitive import Primitive

class Eval (Primitive):
    
    def __init__(self):
        param_rules = (
            (object,),
        )
        super().__init__('any_eval', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        return args[0].eval(etor)
