from alltypes.object import Object

class Integer (Object):

    __slots__ = ('_value',)

    def __init__(self, value):
        self._value = value

    def bool_value(self):
        return self._value != 0

    def __lt__(self, other):
        if not isinstance(other, Integer):
            return repr(self) < repr(other)
        return self._value < other._value

    def __repr__(self):
        return repr(self._value)

    def type_name(self):
        return 'Integer'
