from data.list import List
from object.object import Object

class Queue (Object):

    __slots__ = ('_first', '_last', '_count')

    def __init__(self):
        self._first = None
        self._last = None
        self._count = 0

    @staticmethod
    def from_python_list(python_list):
        queue = Queue()
        for elem in python_list:
            queue.enq(elem)
        return queue

    def as_list(self):
        return self._first

    def deq(self):
        if self._count == 0:
            return None
        elem = self._first.first
        self._first = self._first.rest
        if self._first.rest is None:
            self._last = None
        self._count -= 1

    def enq(self, elem):
        pair = data.list.List.Pair(elem, None)
        if self._count == 0:
            self._first = pair
            self._last = pair
        else:
            self._last.next = pair
            self._last = pair
        self._count += 1

    def type_name(self):
        return 'Queue'

    def __repr__(self):
        return str(self._values)
