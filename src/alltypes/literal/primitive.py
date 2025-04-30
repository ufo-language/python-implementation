from alltypes.expr.identifier import Identifier
from alltypes.object import Object

class Primitive (Object):

    __slots__ = ('_name')

    def __init__(self, name):
        self._name = name

    def apply(self, args, etor):
        ''' Do not override. Override apply_aux instead. '''
        self.check_arg_types(args)
        return self.apply_aux(args, etor)
    
    def apply_aux(self, args, etor):
        ''' Subclasses should override. '''
        pass

    def check_arg_types(self, args):
        pass
    
    def define_prim(self, env):
        env.bind(Identifier(self._name), self)

    def __hash__(self):
        return hash(self._function)

    def __lt__(self, other):
        if not isinstance(other, Primitive):
            return repr(self) < repr(other)
        return self._function < other._function

    def show(self, stream):
        stream.write('Primitive{')
        stream.write(self._name)
        stream.write('}')

    def type_name(self):
        return 'Primitive'
