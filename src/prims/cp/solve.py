from alltypes.literal.nil import Nil
from alltypes.literal.primitive import Primitive

class Solve (Primitive):
    
    def __init__(self):
        super().__init__('solve')

    def check_arg_types(self, args):
        return 0

    def apply_aux(self, args, param_rule_num, etor):
        return Nil()
