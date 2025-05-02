from alltypes.literal.integer import Integer
from alltypes.object import Object
from alltypes.data._show_elems import show_elems
from ufo_exception import UFOException

class Array (Object):

    __slots__ = ('_elems',)

    def __init__(self, elems):
        self._elems = elems

    @staticmethod
    def create(elems):
        return Array(elems)

    @staticmethod
    def from_parser(parse_value):
        return Array(parse_value)

    def bool_value(self):
        return len(self._elems) > 0

    def eval_rec(self, etor):
        elem_values = [etor.eval(elem) for elem in self._elems]
        return Array(elem_values)

    def get(self, index):
        # if type(index) == Integer:
        #     if index._value < 0 or index._value >= len(self._elems):
        #         raise UFOException("Index out of bounds", object=self, object_type=self.type_name(), domain=Array((Integer(0), Integer(len(self._elems)-1))), index=index, index_type=index.type_name())
        #     return self._elems[index._value]
        # raise UFOException("Invalid index type for object", object=self, object_type=self.type_name(), index=index, index_type=index.type_name())
        return Array.get_with_elems(self, self._elems, index)

    @staticmethod
    def get_with_elems(obj, elems, index):
        if type(index) == Integer:
            if index._value < 0 or index._value >= len(elems):
                raise UFOException("Index out of bounds", object=obj, object_type=obj.type_name(), domain=Array((Integer(0), Integer(len(elems)-1))), index=index, index_type=index.type_name())
            return elems[index._value]
        raise UFOException("Invalid index type for object", object=obj, object_type=obj.type_name(), index=index, index_type=index.type_name())
    
    def __iter__(self):
        return iter(self._elems)

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
        self.show_with(stream, '{', ', ', '}')

    def show_with(self, stream, open, sep, close):
        show_elems(stream, self._elems, open, sep, close)

    def type_name(self):
        return 'Array'
