from alltypes.data.array import Array
from alltypes.data.term import Term
from alltypes.expr.identifier import Identifier
from alltypes.literal.nil import Nil
from alltypes.literal.primitive import Primitive
from alltypes.literal.symbol import Symbol

class Variable (Primitive):
    
    def __init__(self):
        param_rules = (
            (Identifier,),
        )
        super().__init__('variable', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        print("cp:variable args=", args)
        return Term(Symbol('Variable'), Array(args))
