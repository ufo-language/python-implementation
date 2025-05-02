from alltypes.literal.primitive import Primitive
from alltypes.literal.symbol import Symbol

class Type (Primitive):
    
    """ Returns the type of an object expressed as a Symbol. """
    
    def __init__(self):
        param_rules = (
            (object,),
        )
        super().__init__('type', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        return Symbol(args[0].type_name())
