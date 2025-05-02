from alltypes.data.hashtable import HashTable
from alltypes.data.queue import Queue
from alltypes.data.set import Set
from alltypes.data.term import Term
from alltypes.literal.string import String
from prims.cp._identifiers import CP_Ident
from ufo_exception import UFOException

class CP_System:

    NEXT_SYSTEM = 0
    ALL_SYSTEMS = {}

    @staticmethod
    def create(args):
        if len(args) == 0:
            name = String(f"CP_SYS_{CP_System.NEXT_SYSTEM:03}")
            CP_System.NEXT_SYSTEM += 1
        else:
            name = args[0]
        if CP_System.ALL_SYSTEMS.get(name) is not None:
            raise UFOException("CP system having that name already exists", name=name)
        # these are the variable names
        variables = Set()
        constraints = Queue()
        system_term = Term.create('CP_System', name=name, variables=variables, constraints=constraints)
        # these are the actual variables
        variable_hash = HashTable()
        system_term.set_attrib(variable_hash)
        CP_System.ALL_SYSTEMS[name] = system_term
        return system_term

    @staticmethod
    def add_constraint(variable, constraint):
        constraints = variable[CP_Ident.CONSTRAINTS]
        constraints.enq(constraint)

    @staticmethod
    def add_variable(system, variable):
        from prims.cp._identifiers import CP_Ident
        from prims.cp._variable import CP_Variable
        variable_name = CP_Variable.name(variable)
        system[CP_Ident.VARIABLES].add(variable_name)
        variables = system.get_attrib()
        variables[variable_name] = variable
