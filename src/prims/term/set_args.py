from alltypes.data.array import Array
from alltypes.data.hashtable import HashTable
from alltypes.data.term import Term
from alltypes.literal.primitive import Primitive

class SetArgs (Primitive):
    
    """ Sets a term's argument data structure. """
    
    def __init__(self):
        param_rules = (
            (Term, Array),
            (Term, HashTable)
        )
        super().__init__('set_args', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        term = args[0]
        args = args[1]
        term.set_args(args)
        return term
