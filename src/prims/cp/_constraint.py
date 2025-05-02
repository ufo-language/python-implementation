class CP_Constraint:
    
    @staticmethod
    def add_to_var(constraint, variable):
        from prims.cp._variable import CP_Variable
        CP_Variable.add_constraint(variable, constraint)
        CP_Constraint.apply_constraint(constraint, variable)
        return variable

    @staticmethod
    def apply_constraint(constraint, variable):
        from prims.cp.variable import CP_Variable
        # get the range
        domain = CP_Variable.domain(variable)
        print("CP_Constraint doimain =", domain)
        # constrain the range based on the constraint
