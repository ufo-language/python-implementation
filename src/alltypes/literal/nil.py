from alltypes.object import Object

class Nil (Object):

    __slots__ = ()

    def __init__(self, _=None):
        pass

    def type_name(self):
        return 'Nil'

    def __lt__(self, other):
        if not isinstance(other, Nil):
            return str(self) < str(other)
        return false

    def __repr__(self):
        return 'nil'
