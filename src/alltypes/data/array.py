from alltypes.object import Object
from alltypes.data._show_elems import show_elems

class Array (Object):

    __slots__ = ('_elems',)

    def __init__(self, elems):
        self._elems = elems

    @staticmethod
    def from_parser(parse_value):
        return Array(parse_value)

    def bool_value(self):
        return len(self._elems) > 0

    def eval_rec(self, etor):
        new_elems = [etor.eval(elem) for elem in self._elems]
        return Array(new_elems)

    def eval_cps(self, etor):
        assert False

    def eval_compile(self, etor):
        assert False

    def pre_bind(self, other, env, binding_pairs):
        if type(other) is not Array:
            return False
        return Array.pre_bind_elems(self._elems, other._elems, env, binding_pairs)

    @staticmethod
    def pre_bind_elems(lhs_elems, rhs_elems, env, binding_pairs):
        if len(lhs_elems) != len(rhs_elems):
            return False
        for (lhs, rhs) in zip(lhs_elems, rhs_elems):
            if not lhs.pre_bind(rhs, env, binding_pairs):
                return False
        return True

    def show(self, stream):
        show_elems(stream, self._elems, '{', ', ', '}')

    def type_name(self):
        return 'Array'
