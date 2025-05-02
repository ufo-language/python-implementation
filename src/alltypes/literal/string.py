from alltypes.object import Object

class String (Object):

    __slots__ = ('_value',)

    def __init__(self, value):
        self._value = value

    def bool_value(self):
        return len(self._value) > 0

    def display(self, stream):
        stream.write(self._value)

    def __eq__(self, other):
        return isinstance(other, String) and self._value == other._value

    def equals_aux(self, other):
        return self._name == other._name

    def __hash__(self):
        return hash(self._value)

    def __lt__(self, other):
        if not isinstance(other, String):
            return self._value < repr(other)
        return self._value < other._value

    def show(self, stream):
        stream.write('"')
        stream.write(self._value)
        stream.write('"')

    def type_name(self):
        return 'String'

    def value(self):
        return self._value
