from alltypes.object import Object

class Nil (Object):

    __slots__ = ()

    def __init__(self, _=None):
        pass

    def bool_value(self):
        return False

    def disp(self, stream):
        pass

    def __hash__(self):
        return 0
    
    def __lt__(self, other):
        if not isinstance(other, Nil):
            return repr(self) < repr(other)
        return False

    def show(self, stream):
        stream.write('nil')

    def type_name(self):
        return 'Nil'
