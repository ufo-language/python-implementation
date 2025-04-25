from alltypes.object import Object

class String (Object):

    __slots__ = ('_value',)

    def __init__(self, value):
        self._value = value

    def bool_value(self):
        return len(self._value) > 0

    def __lt__(self, other):
        if not isinstance(other, String):
            return self._value < repr(other)
        return self._value < other._value

    def __repr__(self):
        return '"' + self._value + '"'

    def __str__(self):
        return self._value

    def type_name(self):
        return 'String'
