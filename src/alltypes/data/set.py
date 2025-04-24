from alltypes.object import Object

class Set (Object):

    __slots__ = ('_set',)

    def __init__(self):
        self._set = set()

    @staticmethod
    def from_python_list(python_list):
        s = Set()
        for elem in python_list:
            s.add(elem)
        return s

    def add(self, elem):
        return self._set.add(elem)

    def type_name(self):
        return 'Set'

    def __repr__(self):
        s = '${'
        elems = sorted(list(self._set))
        first_iter = True
        for elem in elems:
            if first_iter:
                first_iter = False
            else:
                s += ', '
            s += str(elem)
        s += '}'
        return s
