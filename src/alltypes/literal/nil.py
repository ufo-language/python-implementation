from alltypes.object import Object

class Nil (Object):

    __slots__ = ()

    def __init__(self, _=None):
        pass

    def bool_value(self):
        return False

    def __hash__(self):
        return 0
    
    def __lt__(self, other):
        if not isinstance(other, Nil):
            return repr(self) < repr(other)
        return False

    def __repr__(self):
        return 'nil'

    def type_name(self):
        return 'Nil'
