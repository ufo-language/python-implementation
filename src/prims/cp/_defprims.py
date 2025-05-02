from alltypes.data.hashtable import HashTable
from alltypes.expr.identifier import Identifier
from prims.cp.constraint import Constraint
from prims.cp.solve import Solve
from prims.cp.system import System
from prims.cp.variable import Variable

def define_prims(env):
    ns_name = 'cp'
    ns = HashTable()
    env.bind(Identifier(ns_name), ns)
    Constraint().define_prim(ns, ns_name)
    Solve().define_prim(ns, ns_name)
    System().define_prim(ns, ns_name)
    Variable().define_prim(ns, ns_name)
