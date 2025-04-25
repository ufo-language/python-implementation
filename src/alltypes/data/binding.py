from alltypes.object import Object

class Binding (Object):

    __slots__ = ('_lhs', '_rhs')

    def __init__(self, lhs, rhs):
        self._rhs = rhs
        self._lhs = lhs

    @staticmethod
    def from_python_list(python_list):
        return Binding(*python_list)

    def lhs(self):
        return self._lhs

    def rhs(self):
        return self._rhs

    def type_name(self):
        return 'Binding'

    def __repr__(self):
        return str(self._lhs) + ':' + str(self._rhs)
