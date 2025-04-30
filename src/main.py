from etor.etor_recursive import EtorRecursive
from prims.all_prims import define_prims

import logo
import repl.repl

def main():
    logo.logo()
    etor = EtorRecursive()
    define_prims(etor.env())
    repl.repl.run(etor)

if __name__ == '__main__':
    main()
