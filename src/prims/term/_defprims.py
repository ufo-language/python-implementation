from alltypes.data.hashtable import HashTable
from alltypes.expr.identifier import Identifier
from prims.term.args import Args
from prims.term.attrib import Attrib
from prims.term.create import Create
from prims.term.name import Name
from prims.term.set_attrib import SetAttrib
from prims.term.set_args import SetArgs

def define_prims(env):
    ns_name = 'term'
    ns = HashTable()
    env.bind(Identifier(ns_name), ns)
    Args().define_prim(ns, ns_name)
    Attrib().define_prim(ns, ns_name)
    Create().define_prim(ns, ns_name)
    Name().define_prim(ns, ns_name)
    SetAttrib().define_prim(ns, ns_name)
    SetArgs().define_prim(ns, ns_name)
