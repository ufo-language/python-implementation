from alltypes.object import Object

class Symbol (Object):

    __slots__ = ('_name',)

    def __init__(self, name):
        self._name = name

    def type_name(self):
        return 'Symbol'

    def __lt__(self, other):
        if not isinstance(other, Symbol):
            return str(self) < str(other)
        return self._name < other._name

    def __repr__(self):
        return str(self._name)
