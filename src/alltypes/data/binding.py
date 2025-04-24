from alltypes.object import Object

class Binding (Object):

    __slots__ = ('_lhs', '_rhs')

    def __init__(self, lhs, rhs):
        self._rhs = rhs
        self._lhs = lhs

    def type_name(self):
        return 'Binding'

    def __repr__(self):
        return str(self._lhs) + '=' + str(self._rhs)
