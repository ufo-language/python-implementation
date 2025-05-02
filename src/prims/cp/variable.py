from alltypes.data.term import Term
from alltypes.expr.identifier import Identifier
from alltypes.literal.primitive import Primitive
from alltypes.literal.symbol import Symbol
from prims.cp._variable import CP_Variable

class Variable (Primitive):
    
    """ Creates a variable in a constraint system. """
    
    def __init__(self):
        param_rules = (
            (Primitive.term_type('CP_System'), Identifier),
        )
        super().__init__('variable', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        return CP_Variable.create(args)
