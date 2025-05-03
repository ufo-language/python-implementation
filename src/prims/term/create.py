from alltypes.data.array import Array
from alltypes.data.hashtable import HashTable
from alltypes.data.term import Term
from alltypes.literal.nil import Nil
from alltypes.literal.primitive import Primitive
from alltypes.literal.symbol import Symbol

class Create (Primitive):
    
    """ Creates a new term. """
    
    def __init__(self):
        param_rules = (
            (Symbol, (Array, HashTable)),
            (Symbol, (Array, HashTable), object)
        )
        super().__init__('create', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        name = args[0]
        args_structure = args[1]
        if len(args) == 3:
            attrib = args[2]
        else:
            attrib = Nil()
        term = Term(name, args_structure, attrib)
        return term
