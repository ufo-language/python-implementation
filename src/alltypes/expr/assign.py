import alltypes.literal.nil
from alltypes.object import Object

class Assign (Object):

    __slots__ = ('_lhs', '_rhs')

    def __init__(self, lhs, rhs):
        self._lhs = lhs
        self._rhs = rhs

    @staticmethod
    def from_python_list(python_list):
        return Assign(*python_list)

    def eval_rec(self, etor):
        # prebind lhs
        free_var_set = set()
        lhs.free_vars(free_var_set)
        for free_var in free_var_set:
            etor.bind(free_var, free_var)
        # evaluate rhs
        rhs_value = etor.eval(self._rhs)
        # match to lhs
        etor.match_bind(self._lhs, rhs_value)
        return alltypes.literal.nil.Nil()

    def type_name(self):
        return 'Assignment'

    def __repr__(self):
        return str(self._lhs) + " := " + str(self._rhs)
