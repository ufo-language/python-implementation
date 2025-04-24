from alltypes.object import Object

class Symbol (Object):

    __slots__ = ('_value',)

    def __init__(self, value):
        self._value = value

    def type_name(self):
        return 'Symbol'

    def __repr__(self):
        return str(self._value)
