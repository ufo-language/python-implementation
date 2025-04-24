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

    def eval_rec(self, etor):
        return self

    def eval_cps(self, etor):
        return etor.push_expr(self)

    def eval_compile(self, etor):
        return {'PUSH_EXPR', self}

    def type_name(self):
        raise Exception(f"Subclass {self.__class__.__name__} must implement Object.type_name")

