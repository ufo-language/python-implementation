import sys

from alltypes.literal.nil import Nil
from alltypes.literal.primitive import Primitive

class Show (Primitive):
    
    def __init__(self):
        super().__init__('io_show')
        
    def apply_aux(self, args, etor):
        for arg in args:
            arg.show(sys.stdout)
        return Nil()
