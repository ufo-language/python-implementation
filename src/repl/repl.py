import sys
import traceback

import repl.rep

def run(etor):
    repl_state = {'continue': True}
    try:
        while repl_state['continue']:
            input_string = ''
            sys.stdout.write("UFO> ")
            while True:
                line = input()
                if line.endswith('\\'):
                    line = line[:-1].rstrip()
                    input_string += line + '\n'
                    continue
                else:
                    input_string += line
                break
            if input_string.startswith(':'):
                colon_command(input_string, repl_state)
            else:
                repl.rep.rep(input_string, etor)
    except KeyboardInterrupt:
        print()
    except EOFError:
        print()
    except Exception as exn:
        print(traceback.format_exc())

def colon_command(input_string, repl_state):
    match input_string[1]:
        case 'q':
            repl_state['continue'] = False
        case _:
            pass
