from alltypes.data.hashtable import HashTable
from alltypes.data.set import Set
from alltypes.data.term import Term
from alltypes.literal.string import String
from ufo_exception import UFOException

class CP_System:

    NEXT_SYSTEM = 0
    ALL_SYSTEMS = {}

    @staticmethod
    def create(args):
        if len(args) == 0:
            name = String(f"CPSYS{CP_System.NEXT_SYSTEM:03}")
            CP_System.NEXT_SYSTEM += 1
        else:
            name = args[0]
        if CP_System.ALL_SYSTEMS.get(name) is not None:
            raise UFOException("CP system having that name already exists", name=name)
        # these are the variable names
        variables = Set()
        system_term = Term.create('CP_System', name=name, variables=variables)
        # these are the actual variables
        variable_hash = HashTable()
        system_term.set_attrib(variable_hash)
        CP_System.ALL_SYSTEMS[name] = system_term
        return system_term

    @staticmethod
    def add_variable(system, variable):
        from prims.cp._cp_ident import CP_Ident
        from prims.cp._cp_variable import CP_Variable
        variable_name = CP_Variable.name(variable)
        system[CP_Ident.VARIABLES].add(variable_name)
        variables = system.get_attrib()
        variables[variable_name] = variable
