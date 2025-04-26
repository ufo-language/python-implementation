from alltypes.object import Object

class Binding (Object):

    __slots__ = ('_lhs', '_rhs')

    CHAR = ':'

    def __init__(self, lhs, rhs):
        self._rhs = rhs
        self._lhs = lhs

    def eval_rec(self, etor):
        print("Binding.eval is incomplete")
        return self

    @staticmethod
    def from_parser(parse_value):
        return Binding(*parse_value)

    def lhs(self):
        return self._lhs

    def rhs(self):
        return self._rhs

    def type_name(self):
        return 'Binding'

    def __repr__(self):
        return repr(self._lhs) + ':' + repr(self._rhs)
