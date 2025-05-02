from alltypes.literal.integer import Integer
from alltypes.object import Object
from ufo_exception import UFOException

class Range (Object):

    __slots__ = ('_from', '_to', '_by')

    def __init__(self, from_value, to_value, by_value):
        self._from = from_value
        self._to = to_value
        self._by = by_value

    def show(self, stream):
        stream.write('Range(')
        if self._from != 0:
            stream.write(str(self._from))
            stream.write(', ')
        stream.write(str(self._to))
        if self._by.value() != 1:
            stream.write(', ')
            stream.write(str(self._by))
        stream.write(')')

    def type_name(self):
        return 'Range'
