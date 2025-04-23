from object.object import Object

class Float (Object):

    __slots__ = ('_value',)

    def __init__(self, value):
        self._value = value

    def type_name(self):
        return 'Float'

    def __repr__(self):
        return str(self._value)
