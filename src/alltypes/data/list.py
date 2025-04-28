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
        proper_elems = parse_value[0]
        if len(proper_elems) == 0:
            return List.EMPTY_LIST
        improper_elem = parse_value[1]
        first = None
        last = None
        for elem in proper_elems:
            if first is None:
                first = last = List(elem)
            else:
                last._rest = List(elem)
                last = last._rest
        if improper_elem is not None:
            last._rest = improper_elem
        return first

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
    
    def rest(self):
        return self._rest

    def set_first(self, first):
        self._first = first

    def set_rest(self, rest):
        self._rest = rest

    def type_name(self):
        return 'List'

    def show(self, stream):
        self.show_using(self, stream, '[', ', ', ']')

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
