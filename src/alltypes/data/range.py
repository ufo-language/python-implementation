from alltypes.literal.integer import Integer
from alltypes.literal.symbol import Symbol
from alltypes.object import Object
from prims.operators._inf import PLUS_INF

class Range (Object):

    __slots__ = ('_from', '_to', '_by')

    def __init__(self, from_value, to_value, by_value=None):
        self._from = from_value
        self._to = to_value
        self._by = Integer(1) if by_value is None else by_value

    def count(self):
        if type(self._from) is Symbol or type(self._to) is Symbol:
            return PLUS_INF
        from_value = self._from.value()
        to_value = self._to.value()
        by_value = self._by.value()
        if by_value == 0:
            return PLUS_INF
        if (by_value > 0 and from_value > to_value) or (by_value < 0 and from_value < to_value):
            return 0
        return (abs(to_value - from_value) // abs(by_value)) + 1

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
