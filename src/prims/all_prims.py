import prims.any._defprims
import prims.cp._defprims
import prims.io._defprims
import prims.operators._defprims
import prims.prim._defprims

def define_prims(env):
    prims.any._defprims.define_prims(env)
    prims.cp._defprims.define_prims(env)
    prims.io._defprims.define_prims(env)
    prims.operators._defprims.define_prims(env)
    prims.prim._defprims.define_prims(env)
