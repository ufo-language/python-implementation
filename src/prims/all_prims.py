import prims.any._defprims
import prims.cp._defprims
import prims.int._defprims
import prims.io._defprims
import prims.lexer._defprims
import prims.list._defprims
import prims.operators._defprims
import prims.prim._defprims
import prims.queue._defprims
import prims.term._defprims

def define_prims(env):
    prims.any._defprims.define_prims(env)
    prims.cp._defprims.define_prims(env)
    prims.int._defprims.define_prims(env)
    prims.io._defprims.define_prims(env)
    prims.lexer._defprims.define_prims(env)
    prims.list._defprims.define_prims(env)
    prims.operators._defprims.define_prims(env)
    prims.prim._defprims.define_prims(env)
    prims.queue._defprims.define_prims(env)
    prims.term._defprims.define_prims(env)
