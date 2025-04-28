from alltypes.object import Object
from ufo_exception import UFOException

class Identifier (Object):
    
    class ClosedIdentifier (Object):
        
        __slots__ = ('ident', 'index')

        def __init__(self, ident, index):
            self.ident = ident
            self.index = index

        def eval_rec(self, etor):
            return etor.get_env_rel(self.index)
        
        def show(self, stream):
            self.ident.show(stream)

    __slots__ = ('_name', '_hash')

    ALL_IDENTIFIERS = {}

    def __new__(cls, name):
        if name in cls.ALL_IDENTIFIERS:
            return cls.ALL_IDENTIFIERS[name]
        self = super().__new__(cls)
        cls.ALL_IDENTIFIERS[name] = self
        return self

    def __init__(self, name):
        # 'new' calls 'init' even for already-constructed objects
        if not hasattr(self, 'name'):
            self._name = name
            self._hash = hash(name)

    def closure(self, env):
        index = env.lookup_index_rel(self)
        if index is None:
            return self
        return Identifier.ClosedIdentifier(self, index)

    def __eq__(self, other):
        return isinstance(other, Identifier) and self._name == other._name

    def equals(self, other):
        return self._name == other._name

    def eval_rec(self, etor):
        value = etor.lookup(self)
        if value is None:
            raise UFOException(f"Unbound identifier '{self._name}'")
        return value

    def free_vars(self, free_var_set):
        free_var_set.add(self)

    def __hash__(self):
        return self._hash

    def match(self, other, env):
        value = env.lookup(self)
        if value == other:
            return True
        env.bind(self, other)
        return True

    def show(self, stream):
        stream.write(self._name)

    def type_name(self):
        return 'Assignment'
