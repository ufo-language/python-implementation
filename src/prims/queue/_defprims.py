from alltypes.data.hashtable import HashTable
from alltypes.expr.identifier import Identifier
from prims.queue.deq import Deq
from prims.queue.enq import Enq
from prims.queue.length import Length

def define_prims(env):
    ns_name = 'queue'
    ns = HashTable()
    env.bind(Identifier(ns_name), ns)
    Deq().define_prim(ns, ns_name)
    Enq().define_prim(ns, ns_name)
    Length().define_prim(ns, ns_name)
