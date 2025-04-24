from alltypes.object import Object

class Nil (Object):

    __slots__ = ()

    def __init__(self, _=None):
        pass

    def bool_value(self):
        return False

    def __lt__(self, other):
        if not isinstance(other, Nil):
            return str(self) < str(other)
        return false

    def __repr__(self):
        return 'nil'

    def type_name(self):
        return 'Nil'
