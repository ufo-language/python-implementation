from alltypes.data.hashtable import HashTable
from alltypes.expr.identifier import Identifier
from prims.prim.help import Help

def define_prims(env):
    ns_name = 'prim'
    ns = HashTable()
    env.bind(Identifier(ns_name), ns)
    Help().define_prim(ns, ns_name)
