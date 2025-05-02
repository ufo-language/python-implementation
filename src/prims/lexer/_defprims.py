from alltypes.data.hashtable import HashTable
from alltypes.expr.identifier import Identifier
from prims.lexer.tokenize import Tokenize

def define_prims(env):
    ns_name = 'lexer'
    ns = HashTable()
    env.bind(Identifier(ns_name), ns)
    Tokenize().define_prim(ns, ns_name)
