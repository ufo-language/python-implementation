from alltypes.literal.primitive import Primitive
from alltypes.literal.string import String
from prims.cp._cp_system import CP_System

class System (Primitive):

    def __init__(self):
        param_rules = (
            (),
            (String,)
        )
        super().__init__('system', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        return CP_System.create(args)
