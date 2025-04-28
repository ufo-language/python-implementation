class Environment:

    class Binding:
        __slots__ = ('lhs', 'rhs')

        def __init__(self, lhs, rhs):
            self.lhs = lhs
            self.rhs = rhs
    
    __slots__ = ('_bindings',)

    def __init__(self):
        self._bindings = []

    def bind(self, ident, value):
        self._bindings.append(Environment.Binding(ident, value))

    def count(self):
        return len(self._bindings)

    def drop(self, n):
        self._bindings[-n:] = []

    def locate_binding_abs(self, ident):
        n = 0
        for binding in self._bindings:
            if binding.lhs == ident:
                return binding
            n += 1
        return None

    def locate_binding_rel(self, ident):
        for n in range(len(self._bindings) - 1, -1, -1):
            binding = self._bindings[n]
            if binding.lhs == ident:
                return binding
        return None
    
    def lookup(self, ident):
        binding = self.locate_binding_rel(ident)
        if binding is not None:
            return binding.rhs
        return None

    def lookup_index_abs(self, ident):
        n = 0
        for binding in self._bindings:
            if binding.lhs == ident:
                return n
            n += 1
        return None

    def lookup_index_rel(self, ident):
        for n in range(-1, -len(self._bindings)-1, -1):
            binding = self._bindings[n]
            if binding.lhs == ident:
                return n
        return None
    
    def rebind_rel(self, ident, value):
        binding = self.locate_binding_rel(ident)
        binding.rhs = value

    def restore(self, n):
        ''' Restore (reduce) the environment to have only the first n bindings. '''
        diff = len(self._bindings) - n
        if diff > 0:
            self.drop(n)

    def __repr__(self):
        return repr(self._bindings)

    def save(self):
        return len(self._bindings)
