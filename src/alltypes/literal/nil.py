from object.object import Object

class Nil (Object):

    __slots__ = ()

    def __init__(self, _=None):
        pass

    def type_name(self):
        return 'Nil'

    def __repr__(self):
        return 'nil'
