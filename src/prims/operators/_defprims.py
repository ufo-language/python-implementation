from prims.operators.equals import Equals
from prims.operators.plus import Plus

def define_prims(env):
    Equals().define_prim(env)
    Plus().define_prim(env)
