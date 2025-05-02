import sys

from alltypes.literal.nil import Nil
from alltypes.literal.primitive import Primitive

class Display (Primitive):

    """ Displays one or more values. """
    
    def __init__(self):
        super().__init__('disp')

    def check_arg_types(self, args):
        return 0

    def apply_aux(self, args, param_rule_num, etor):
        for arg in args:
            arg.display(sys.stdout)
        return Nil()
