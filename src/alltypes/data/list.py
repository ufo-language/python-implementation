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
    def create(elems, improper_elem=None):
        if len(elems) == 0:
            return List.EMPTY_LIST
        first = None
        last = None
        for elem in elems:
            if first is None:
                first = last = List(elem)
            else:
                last._rest = List(elem)
                last = last._rest
        if improper_elem is not None:
            last._rest = improper_elem
        return first

    @staticmethod
    def from_parser(parse_value):
        proper_elems = parse_value[0]
        improper_elem = parse_value[1]
        return List.create(proper_elems, improper_elem)

    def bool_value(self):
        return not self.is_empty()

    def eval_rec(self, etor):
        lst = self
        first = None
        last = None
        while not lst.is_empty():
            elem = lst._first
            elem_value = etor.eval(elem)
            pair = List(elem_value)
            if first is None:
                first = last = pair
            else:
                last.set_rest(pair)
                last = pair
            lst = lst._rest
            if not isinstance(lst, List):
                elem_value = etor.eval(lst)
                last.set_rest(elem_value)
                break
        return first
    
    def first(self):
        return self._first

    def is_empty(self):
        return self is List.EMPTY_LIST
    
    def length(self):
        n_elems = 0
        lst = self
        while not lst.is_empty():
            n_elems += 1
            lst = lst._rest
            if type(lst) is not List:
                n_elems += 1
                break
        return n_elems

    def match(self, other, env):
        if type(other) is not List:
            return False
        self1 = self
        other1 = other
        while True:
            self_empty = self1.is_empty()
            other_empty = other1.is_empty()
            if self_empty and other_empty:
                return True
            if self_empty or other_empty:
                return False
            if not self1._first.match(other1._first, env):
                return False
            self_rest = self1._rest
            other_rest = other1._rest
            if type(self_rest) is not List:
                return self_rest.match(other_rest, env)
            if type(other_rest) is not List:
                return False
            self1 = self_rest
            other1 = other_rest

    def rest(self):
        return self._rest

    def set_first(self, first):
        self._first = first

    def set_rest(self, rest):
        self._rest = rest

    def type_name(self):
        return 'List'

    def show(self, stream):
        self.show_using(stream, '[', ', ', ']')

    def show_using(self, stream, open, sep, close):
        stream.write(open)
        lst = self
        first_iter = True
        while not lst.is_empty():
            if first_iter:
                first_iter = False
            else:
                stream.write(sep)
            elem = lst._first
            elem.show(stream)
            lst = lst._rest
            if not isinstance(lst, List):
                stream.write(' | ')
                lst.show(stream)
                break
        stream.write(close)

List.EMPTY_LIST = List(None, None)
