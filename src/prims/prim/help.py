from alltypes.data.hashtable import HashTable
from alltypes.literal.primitive import Primitive
from alltypes.literal.string import String

class Help (Primitive):
    
    """ Returns help and parameter type information for a primitive. """
    
    def __init__(self):
        param_rules = (
            (Primitive,),
        )
        super().__init__('help', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        prim = args[0]
        param_types = Primitive.param_rules_demangle(prim.param_rules())
        return HashTable.create(about=String(prim.about()), param_types=param_types)
