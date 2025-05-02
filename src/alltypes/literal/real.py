from alltypes.object import Object

class Real (Object):

    __slots__ = ('_value',)

    def __init__(self, value):
        self._value = value

    def bool_value(self):
        return self._value != 0.0

    def __eq__(self, other):
        return isinstance(other, Real) and self._value == other._value

    def equals_aux(self, other):
        return self._value == other._value

    def __hash__(self):
        return hash(self._value)

    def __lt__(self, other):
        if not isinstance(other, Real):
            return repr(self) < repr(other)
        return self._value < other._value

    def show(self, stream):
        stream.write(str(self._value))

    def type_name(self):
        return 'Real'
