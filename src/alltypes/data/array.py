from object.object import Object

class Array (Object):

    __slots__ = ('_elems',)

    def __init__(self, elems):
        self._elems = elems

    def type_name(self):
        return 'Array'

    def __repr__(self):
        s = '{'
        first_iter = True
        for elem in self._elems:
            if first_iter:
                first_iter = False
            else:
                s += ', '
            s += str(elem)
        s += '}'
        return s
