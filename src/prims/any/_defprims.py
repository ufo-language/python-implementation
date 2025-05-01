from alltypes.data.hashtable import HashTable
from alltypes.expr.identifier import Identifier
from prims.any.eval import Eval

def define_prims(env):
    ns_name = 'any'
    ns = HashTable()
    env.bind(Identifier(ns_name), ns)
    Eval().define_prim(ns, ns_name)
