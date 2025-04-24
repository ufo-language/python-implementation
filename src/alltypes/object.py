class Object:

    __slots__ = ()

    def eval(self, etor):
        match etor.type:
            case 'RECURSIVE':
                return self.eval_rec(etor)
            case 'CPS':
                return self.eval_cps(etor)
            case 'COMPILER':
                return self.eval_compile(etor)

    def __eq__(self, other):
        return self.equals(other)

    def equals(self, other):
        ''' Override equals_aux instead of this method. '''
        if type(self) != type(other):
            return false
        return self.equals_aux(other)

    def equals_aux(self, other):
        ''' Override this one. '''
        return self is other

    def eval_rec(self, etor):
        return self

    def eval_cps(self, etor):
        return etor.push_expr(self)

    def eval_compile(self, etor):
        return {'PUSH_EXPR', self}

    def match(self, other, env):
        print("Object.match self =", self, "other =", other)
        if self == other:
            return env
        return None

    def type_name(self):
        raise Exception(f"Subclass {self.__class__.__name__} must implement Object.type_name")
