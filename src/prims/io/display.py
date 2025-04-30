import sys

from alltypes.literal.nil import Nil
from alltypes.literal.primitive import Primitive

class Display (Primitive):
    
    def __init__(self):
        super().__init__('io_disp')

    def check_arg_types(self, args):
        return 0

    def apply_aux(self, args, param_rule_num, etor):
        for arg in args:
            arg.display(sys.stdout)
        return Nil()
