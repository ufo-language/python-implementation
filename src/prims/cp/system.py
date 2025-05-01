from alltypes.data.array import Array
from alltypes.data.term import Term
from alltypes.literal.nil import Nil
from alltypes.literal.primitive import Primitive
from alltypes.literal.symbol import Symbol

class System (Primitive):
    
    def __init__(self):
        super().__init__('system')

    def apply_aux(self, args, param_rule_num, etor):
        return Term(Symbol('CP_System'), Array([]))