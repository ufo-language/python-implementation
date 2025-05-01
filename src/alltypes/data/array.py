from alltypes.literal.integer import Integer
from alltypes.object import Object
from alltypes.data._show_elems import show_elems
from ufo_exception import UFOException

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

    def get(self, index):
        if type(index) == Integer:
            if index._value < 0 or index._value >= len(self._elems):
                raise UFOException("Index out of bounds", object=self, object_type=self.type_name(), domain=Array((Integer(0), Integer(len(self._elems)-1))), index=index, index_type=index.type_name())
            return self._elems[index._value]
        raise UFOException("Invalid index type for object", object=self, object_type=self.type_name(), index=index, index_type=index.type_name())

    def match(self, other, env):
        if type(other) is not Array:
            return False
        return Array.match_elems(self._elems, other._elems, env)

    @staticmethod
    def match_elems(lhs_elems, rhs_elems, env):
        if len(lhs_elems) != len(rhs_elems):
            return False
        for (lhs, rhs) in zip(lhs_elems, rhs_elems):
            if not lhs.match(rhs, env):
                return False
        return True

    def show(self, stream):
        show_elems(stream, self._elems, '{', ', ', '}')

    def type_name(self):
        return 'Array'
