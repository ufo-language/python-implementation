import alltypes.data.queue
from alltypes.object import Object

class List (Object):

    __slots__ = ('_first', '_rest')

    EMPTY_LIST = None

    def __init__(self, first, rest=None):
        self._first = first
        if rest is None:
            rest = List.EMPTY_LIST
        self._rest = rest

    @staticmethod
    def from_parser(parse_value):
        proper_elems = [parse_value[0]] + parse_value[1]
        queue = alltypes.data.queue.Queue.from_python_list(proper_elems)
        lst = queue.as_list()
        if len(parse_value) > 2:
            last_elem = queue._last
            last_elem.set_rest(parse_value[2])
        return lst

    def bool_value(self):
        return not self.is_empty()

    def is_empty(self):
        return self is List.EMPTY_LIST

    def set_first(self, first):
        self._first = first

    def set_rest(self, rest):
        self._rest = rest

    def type_name(self):
        return 'List'

    def repr_using(self, open, sep, close):
        s = open
        lst = self
        first_iter = True
        while not lst.is_empty():
            if first_iter:
                first_iter = False
            else:
                s += sep
            elem = lst._first
            s += repr(elem)
            lst = lst._rest
            if not isinstance(lst, List):
                s += ' | ' + repr(lst)
                break
        s += close
        return s

    def __repr__(self):
        return self.repr_using('[', ', ', ']')

List.EMPTY_LIST = List(None, None)
