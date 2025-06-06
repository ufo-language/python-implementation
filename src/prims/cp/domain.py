from alltypes.data.term import Term
from alltypes.literal.nil import Nil
from alltypes.literal.primitive import Primitive
from prims.cp.variable import CP_Variable

class Domain (Primitive):

    """ Gets or sets a variable's domain. """

    def __init__(self):
        is_variable = Primitive.term_type('CP_Variable')
        param_rules = (
            (is_variable,),
            (is_variable, object),
        )
        super().__init__('domain', param_rules)

    def apply_aux(self, args, param_rule_num, etor):
        variable = args[0]
        match param_rule_num:
            case 0:
                return CP_Variable.get_domain(variable)
            case 1:
                domain = args[1]
                CP_Variable.set_domain(variable, domain)
                return variable
            case _:
                raise SystemError(f"Unhandled case {param_rule_num}")
