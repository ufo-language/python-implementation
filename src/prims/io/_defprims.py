from alltypes.data.hashtable import HashTable
from alltypes.expr.identifier import Identifier
from prims.io.display import Display
from prims.io.show import Show

def define_prims(env):
    ns_name = 'io'
    ns = HashTable()
    env.bind(Identifier(ns_name), ns)
    Display().define_prim(ns, ns_name)
    Show().define_prim(ns, ns_name)
