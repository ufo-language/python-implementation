from alltypes.data.hashtable import HashTable
from alltypes.expr.identifier import Identifier
from prims.any.construct import Construct
from prims.any.count import Count
from prims.any.eval import Eval
from prims.any.parts import Parts
from prims.any.type import Type

def define_prims(env):
    ns_name = 'any'
    ns = HashTable()
    env.bind(Identifier(ns_name), ns)
    Construct().define_prim(ns, ns_name)
    Count().define_prim(ns, ns_name)
    Eval().define_prim(ns, ns_name)
    Parts().define_prim(ns, ns_name)
    Type().define_prim(ns, ns_name)
