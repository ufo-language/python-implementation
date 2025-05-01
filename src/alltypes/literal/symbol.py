from alltypes.object import Object

class Symbol (Object):

    __slots__ = ('_name', '_hash')

    ALL_SYMBOLS = {}

    def __new__(cls, name):
        if name in cls.ALL_SYMBOLS:
            return cls.ALL_SYMBOLS[name]
        self = super().__new__(cls)
        cls.ALL_SYMBOLS[name] = self
        return self

    def __init__(self, name):
        # 'new' calls 'init' even for already-constructed objects
        if not hasattr(self, '_name'):
            self._name = name
            self._hash = hash(name)

    def __eq__(self, other):
        return isinstance(other, Symbol) and self._name == other._name

    def equals_aux(self, other):
        return self._name == other._name

    def __hash__(self):
        return self._hash

    def __lt__(self, other):
        if not isinstance(other, Symbol):
            return self._name < repr(other)
        return self._name < other._name
    
    def name(self):
        return self._name

    def show(self, stream):
        stream.write(self._name)

    def type_name(self):
        return 'Symbol'
