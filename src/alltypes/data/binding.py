from alltypes.object import Object

class Binding (Object):

    __slots__ = ('_lhs', '_rhs')

    CHAR = ':'

    def __init__(self, lhs, rhs):
        self._rhs = rhs
        self._lhs = lhs

    def eval_rec(self, etor):
        return Binding(etor.eval(self._lhs), etor.eval(self._rhs))

    @staticmethod
    def from_parser(parse_value):
        return Binding(*parse_value)

    def lhs(self):
        return self._lhs

    def match(self, other, env):
        if type(other) is not Binding:
            return False
        return self._lhs.match(other._lhs, env) and self._rhs.match(other._rhs, env)

    def rhs(self):
        return self._rhs
    
    def show(self, stream):
        self._lhs.show(stream)
        stream.write(':')
        self._rhs.show(stream)

    def type_name(self):
        return 'Binding'
