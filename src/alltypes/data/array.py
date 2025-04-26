from alltypes.object import Object

class Array (Object):

    __slots__ = ('_elems',)

    def __init__(self, elems):
        self._elems = elems

    @staticmethod
    def from_parser(parse_value):
        if len(parse_value) > 0:
            (first, rest) = parse_value
            elems = [first] + rest
        else:
            elems = []
        return Array(elems)

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

    def type_name(self):
        return 'Array'

    def __repr__(self):
        s = '{'
        first_iter = True
        for elem in self._elems:
            if first_iter:
                first_iter = False
            else:
                s += ', '
            s += repr(elem)
        s += '}'
        return s
