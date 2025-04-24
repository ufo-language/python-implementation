from alltypes.object import Object

class Identifier (Object):

    __slots__ = ('_name',)

    def __init__(self, name):
        self._name = name

    @staticmethod
    def from_python_list(python_list):
        return Assign(*python_list)

    def eval_rec(self, etor):
        value = etor.lookup(self._name)
        if value is None:
            raise Exception(f"Unbound identifier '{self._name}'")
        return value

    def match(self, other, env):
        binding = env.lookup(self)
        if binding is not None:
            if binding.rhs() == other:
                return
        env.bind(self, other)

    def type_name(self):
        return 'Assignment'

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
