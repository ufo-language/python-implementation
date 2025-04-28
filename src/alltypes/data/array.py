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
        new_elems = []
        for elem in self._elems:
            new_elems.append(etor.eval(elem))
        return Array(new_elems)

    def eval_cps(self, etor):
        assert False

    def eval_compile(self, etor):
        assert False

    def show(self, stream):
        show_elems(stream, self._elems, '{', ', ', '}')

    def type_name(self):
        return 'Array'
