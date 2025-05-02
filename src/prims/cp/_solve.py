from functools import cmp_to_key

from alltypes.literal.nil import Nil
from prims.cp._system import CP_System
from prims.cp._variable import CP_Variable
# from prims.cp._identifiers import CP_Ident
from prims.operators._inf import MINUS_INF, PLUS_INF

class CP_Solve:
    
    @staticmethod
    def solve(system):
        variables = CP_System.variables(system)
        constraints = CP_System.constraints(system)
        sorted_variables = CP_Solve.sorted_variables(variables)
        print("solve ordered_variables =", sorted_variables)
        combinations = CP_Solve.domain_combinations(sorted_variables)
        return Nil()
 
    @staticmethod
    def domain_combinations(sorted_variables):
        pass

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
            if a_count is MINUS_INF:
                if b_count is MINUS_INF:
                    return 0
                return -1
            if a_count is PLUS_INF:
                if b_count is PLUS_INF:
                    return 0
                return 1
            if b_count is MINUS_INF:
                return 1
            if b_count is PLUS_INF:
                return -1
            return a_count - b_count
        sorted_lst = sorted(var_sizes, key=cmp_to_key(custom_cmp))
        return sorted_lst
