from alltypes.data._show_elems import show_elems
from alltypes.object import Object

class Set (Object):

    __slots__ = ('_set',)

    def __init__(self, *elems):
        self._set = set()
        for elem in elems:
            self.add(elem)

    def eval_rec(self, etor):
        s = Set()
        for elem in self._set:
            elem_value = etor.eval(elem)
            s._set.add(elem_value)
        return s

    @staticmethod
    def from_parser(parse_value):
        return Set(*parse_value)

    def add(self, elem):
        return self._set.add(elem)

    def bool_value(self):
        return not self.is_empty()

    def is_empty(self):
        return len(self._set) > 0

    def type_name(self):
        return 'Set'
    
    def show(self, stream):
        show_elems(stream, self._set, '${', ', ', '}')

    def type_name(self):
        return 'Set'
