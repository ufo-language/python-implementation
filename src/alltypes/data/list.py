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
    def from_python_list(python_list):
        queue = alltypes.data.queue.Queue.from_python_list(python_list)
        return queue.as_list()

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
            s += str(elem)
            lst = lst._rest
        s += close
        return s

    def __repr__(self):
        return self.repr_using('[', ', ', ']')

List.EMPTY_LIST = List(None, None)
