from etor.etor_recursive import EtorRecursive
import logo
import repl.repl

def main():
    logo.logo()
    etor = EtorRecursive()
    repl.repl.run(etor)

if __name__ == '__main__':
    main()
