import alltypes.data.list
from alltypes.object import Object

class Queue (Object):

    __slots__ = ('_first', '_last', '_count')

    def __init__(self):
        self._first = None
        self._last = None
        self._count = 0

    def eval_rec(self, etor):
        print("Queue.eval is incomplete")
        return self

    @staticmethod
    def from_python_list(python_list):
        queue = Queue()
        for elem in python_list:
            queue.enq(elem)
        return queue

    def as_list(self):
        return self._first

    def bool_value(self):
        return not self.is_empty()

    def deq(self):
        if self._count == 0:
            return None
        elem = self._first.first
        self._first = self._first.rest
        if self._first.rest is None:
            self._last = None
        self._count -= 1

    def enq(self, elem):
        pair = alltypes.data.list.List(elem)
        if self._count == 0:
            self._first = pair
        else:
            self._last.set_rest(pair)
        self._last = pair
        self._count += 1

    def type_name(self):
        return 'Queue'

    def __repr__(self):
        return self._first.repr_using('~[', ', ', ']')
