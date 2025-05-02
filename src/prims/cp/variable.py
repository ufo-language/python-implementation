from alltypes.data.term import Term
from alltypes.expr.identifier import Identifier
from alltypes.literal.primitive import Primitive
from alltypes.literal.symbol import Symbol
from prims.cp._cp_variable import CP_Variable

def term_type(name):
    symbol = Symbol(name)
    def fun(term):
        return type(term) == Term and term.name() is symbol
    fun.term_name = symbol
    return fun

class Variable (Primitive):
    
    def __init__(self):
        param_rules = (
            (term_type('CP_System'), Identifier),
        )
        super().__init__('variable', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        return CP_Variable.create(args)
