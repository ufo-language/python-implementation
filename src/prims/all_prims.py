import prims.any._defprims
import prims.io._defprims
import prims.operators._defprims

def define_prims(env):
    prims.any._defprims.define_prims(env)
    prims.io._defprims.define_prims(env)
    prims.operators._defprims.define_prims(env)
