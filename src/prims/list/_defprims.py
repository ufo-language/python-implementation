from alltypes.data.hashtable import HashTable
from alltypes.expr.identifier import Identifier
from prims.list.length import Length
from prims.list.first import First
from prims.list.rest import Rest
from prims.list.set_rest import SetRest

def define_prims(env):
    ns_name = 'list'
    ns = HashTable()
    env.bind(Identifier(ns_name), ns)
    First().define_prim(ns, ns_name)
    Length().define_prim(ns, ns_name)
    Rest().define_prim(ns, ns_name)
    SetRest().define_prim(ns, ns_name)
