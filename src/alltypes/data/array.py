from object.object import Object

class Array (Object):

    __slots__ = ('_values',)

    def __init__(self, values):
        self._values = values

    def type_name(self):
        return 'List'

    def __repr__(self):
        return str(self._values)
