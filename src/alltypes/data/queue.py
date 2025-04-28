from alltypes.data.list import List
from alltypes.object import Object

class Queue (Object):

    __slots__ = ('_first', '_last', '_count')

    def __init__(self, *elems):
        self._first = None
        self._last = None
        self._count = 0
        for elem in elems:
            self.enq(elem)

    def eval_rec(self, etor):
        print("Queue.eval is incomplete")
        return self

    @staticmethod
    def from_parser(parser_value):
        return Queue(*parser_value)

    def as_list(self):
        if self._count == 0:
            return List.EMPTY_LIST
        return self._first

    def bool_value(self):
        return not self.is_empty()

    def deq(self):
        if self._count == 0:
            return None
        # elem = self._first.first
        self._first = self._first.rest
        if self._first.rest is None:
            self._last = None
        self._count -= 1

    def enq(self, elem):
        pair = List(elem)
        if self._first is None:
            self._first = self._last = pair
        else:
            self._last.set_rest(pair)
        self._last = pair
        self._count += 1

    def eval_rec(self, etor):
        q = Queue()
        lst = self._first
        while not lst.is_empty():
            elem = lst.first()
            elem_value = etor.eval(elem)
            q.enq(elem_value)
            lst = lst.rest()
        return q
    
    def show(self, stream):
        if self._count == 0:
            stream.write('~[]')
        else:
            self._first.show_using(stream, '~[', ', ', ']')

    def type_name(self):
        return 'Queue'
