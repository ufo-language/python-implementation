from alltypes.object import Object

class Boolean (Object):

    __slots__ = ('_value',)

    def __init__(self, value):
        self._value = value

    def bool_value(self):
        return self._value
    
    def __eq__(self, other):
        return isinstance(other, Boolean) and self._value == other._value

    def equals_aux(self, other):
        return self._value == other._value

    def __hash__(self):
        return hash(self._value)

    def __lt__(self, other):
        if not isinstance(other, Boolean):
            return repr(self) < repr(other)
        return self._value < other._value
    
    def show(self, stream):
        stream.write('true' if self._value else 'false')

    def type_name(self):
        return 'Boolean'
