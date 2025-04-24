class Environment:

    __slots__ = ('_bindings',)

    def __init__(self):
        self._bindings = []

    def bind(self, ident, value):
        self._bindings.append((ident, value))

    def count(self):
        return len(self._bindings)

    def drop(self, n):
        self._bindings[-n:] = []

    def locate_binding(self, ident):
        n = 0
        for binding in self._bindings:
            if binding[0] == ident:
                return binding
            n += 1
        return None

    def locate_index_abs(self, ident):
        n = 0
        for binding in self._bindings:
            if binding[0] == ident:
                return n
            n += 1
        return -1

    def lookup(self, ident):
        binding = self.locate_binding(ident)
        if binding is not None:
            return binding[1]
        return None

    def save(self):
        return len(self._bindings)

    def restore(self, n):
        ''' Restore (reduce) the environment to have only the first n bindings. '''
        diff = len(self._bindings) - n
        if diff > 0:
            self.drop(n)

    def __repr__(self):
        return str(self._bindings)
