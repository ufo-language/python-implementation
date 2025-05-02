from alltypes.data.hashtable import HashTable
from alltypes.expr.identifier import Identifier
from prims.int.range import Int_Range

def define_prims(env):
    ns_name = 'int'
    ns = HashTable()
    env.bind(Identifier(ns_name), ns)
    Int_Range().define_prim(ns, ns_name)
