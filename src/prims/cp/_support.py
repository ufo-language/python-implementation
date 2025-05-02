from alltypes.data.hashtable import HashTable
from alltypes.data.queue import Queue
from alltypes.data.set import Set
from alltypes.data.term import Term
from alltypes.expr.identifier import Identifier
from alltypes.literal.string import String
from ufo_exception import UFOException

class CP_System:

    NEXT_SYSTEM = 0
    ALL_SYSTEMS = {}

    ID_CONSTRAINTS = Identifier('constraints')
    ID_NAME = Identifier('name')
    ID_VARIABLES = Identifier('variables')

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
        variable_name = CP_Variable.name(variable)
        system[CP_System.ID_VARIABLES].add(variable_name)
        variables = system.get_attrib()
        variables[variable_name] = variable

class CP_Variable:
    
    @staticmethod
    def create(args):
        system = args[0]
        var_name = args[1]
        constraints = Queue()
        variable = Term.create('CP_Variable', name=var_name, constraints=constraints)
        variable.set_attrib(system)
        CP_System.add_variable(system, variable)
        return variable
    
    @staticmethod
    def add_constraint(variable, constraint):
        constraints = variable[CP_System.ID_CONSTRAINTS]
        constraints.enq(constraint)
    
    @staticmethod
    def name(variable):
        return variable[CP_System.ID_NAME]

class CP_Constraint:
    
    @staticmethod
    def add_to_var(constraint, variable):
        CP_Variable.add_constraint(variable, constraint)
        return variable
