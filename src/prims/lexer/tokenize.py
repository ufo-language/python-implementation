from alltypes.data.array import Array
from alltypes.data.queue import Queue
from alltypes.data.term import Term
from alltypes.literal.string import String
from alltypes.literal.symbol import Symbol
from alltypes.literal.primitive import Primitive
from lexer.ufo_syntax import tokenize

class Tokenize (Primitive):
    
    """ Tokenizes a string using the standard UFO syntax. """
    
    def __init__(self):
        param_rules = (
            (String,),
        )
        super().__init__('tokenize', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        string = args[0]
        tokens = tokenize(string.value())
        # The value is a list of tuples. Convert to a Queue of Arrays.
        token_q = Queue()
        for token in tokens:
            name = token[0]
            value = token[1]
            pos = token[2]
            term = Term(Symbol(name), Array([String(value)]), Array(pos[1:]))
            token_q.enq(term)
        return token_q
