from alltypes.literal.nil import Nil
from prims.cp._system import CP_System
from prims.cp._variable import CP_Variable
# from prims.cp._identifiers import CP_Ident

class CP_Solve:
    
    @staticmethod
    def solve(system):
        print("Solve got system", system)
        variables = CP_System.variables(system)
        print("  variables =", variables)
        for variable in variables:
            print("    variable=", variable)
            name = CP_Variable.name(variable)
            domain = CP_Variable.domain(variable)
            print("      name =", name)
            print("      domain =", domain)
            print("      domain count =", domain.count())
        constraints = CP_System.constraints(system)
        print("  constraints =", constraints)
        return Nil()
 