from alltypes.object import Object
from etor.ufo_exception import UFOException

class Identifier (Object):

    __slots__ = ('_name',)

    def __init__(self, name):
        self._name = name

    @staticmethod
    def from_python_list(python_list):
        return Assign(*python_list)

    def equals(self, other):
        return self._name == other._name

    def eval_rec(self, etor):
        value = etor.lookup(self)
        if value is None:
            raise UFOException(f"Unbound identifier '{self._name}'")
        return value

    def match(self, other, env):
        value = env.lookup(self)
        if value == other:
            return True
        env.bind(self, other)
        return True

    def type_name(self):
        return 'Assignment'

    def __repr__(self):
        return self._name