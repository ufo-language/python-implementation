from alltypes.literal.primitive import Primitive

class Eval (Primitive):
    
    """ Evaluates an expression. """
    
    def __init__(self):
        param_rules = (
            (object,),
        )
        super().__init__('eval', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        return args[0].eval(etor)
