from alltypes.object import Object

class Integer (Object):

    __slots__ = ('_value',)

    def __init__(self, value):
        self._value = value

    def __lt__(self, other):
        if not isinstance(other, Integer):
            return str(self) < str(other)
        return self._value < other._value

    def type_name(self):
        return 'Integer'

    def __repr__(self):
        return str(self._value)
