from alltypes.data.queue import Queue
from object.object import Object

class List (Object):

    class Pair:
        __slots__ = ('first', 'rest')
        def __init__(self, first, rest):
            self._first = first
            self._rest = rest

    __slots__ = ('_values',)

    def __init__(self, first, rest=None):
        self._first = first
        if rest is None:
            rest = EMPTY_LIST
        self._rest = rest

    @staticmethod
    def from_python_list(python_list):
        queue = Queue.from_python_list(python_list)
        return queue.as_list()

    def is_empty(self):
        return self == EMPTY_LIST

    def type_name(self):
        return 'List'

    def __repr__(self):
        s = '['
        list = self._first
        while 
        return str(self._values)

EMPTY_LIST = List(None, None)
