from alltypes.object import Object

class Boolean (Object):

    __slots__ = ('_value',)

    def __init__(self, value):
        self._value = value

    def type_name(self):
        return 'Boolean'

    def __lt__(self, other):
        if not isinstance(other, Boolean):
            return str(self) < str(other)
        return self._value < other._value

    def __repr__(self):
        return 'true' if self._value else 'false'
