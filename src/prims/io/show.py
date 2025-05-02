import sys

from alltypes.literal.nil import Nil
from alltypes.literal.primitive import Primitive

class Show (Primitive):

    """ Shows one or more values. """

    def __init__(self):
        super().__init__('show')
        
    def check_arg_types(self, args):
        return 0

    def apply_aux(self, args, param_rule_num, etor):
        for arg in args:
            arg.show(sys.stdout)
        return Nil()
