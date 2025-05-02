from functools import cmp_to_key
from itertools import product

from alltypes.literal.nil import Nil
from prims.cp._system import CP_System
from prims.cp._variable import CP_Variable
# from prims.cp._identifiers import CP_Ident

class CP_Solve:
    
    @staticmethod
    def solve(system):
        variables = CP_System.variables(system)
        constraints = CP_System.constraints(system)
        sorted_variables = CP_Solve.sorted_variables(variables)
        print("solve ordered_variables =", sorted_variables)
        combinations = CP_Solve.domain_combinations(sorted_variables)
        for combination in combinations:
            print("combination =", combination)
        return Nil()
 
    @staticmethod
    def domain_combinations(sorted_variables):
        names = [CP_Variable.name(var) for _, var in sorted_variables]
        domains = [list(CP_Variable.domain(var)) for _, var in sorted_variables]
        for values in product(*domains):
            yield dict(zip(names, values))

    @staticmethod
    def sorted_variables(variables):
        # order the variables by domain size
        var_sizes = []
        for variable in variables:
            domain = CP_Variable.domain(variable)
            var_sizes.append((domain.count(), variable))
        def custom_cmp(a, b):
            a_count = a[0]
            b_count = b[0]
            return a_count - b_count
        sorted_lst = sorted(var_sizes, key=cmp_to_key(custom_cmp))
        return sorted_lst
