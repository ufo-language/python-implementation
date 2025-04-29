import io

class Object:

    __slots__ = ()

    def bool_value(self):
        return True

    def closure(self):
        return self

    def disp(self, stream):
        self.show(stream)

    def __eq__(self, other):
        return self.equals(other)

    def equals(self, other):
        ''' Override equals_aux() instead of this method. '''
        if type(self) != type(other):
            return False
        return self.equals_aux(other)

    def equals_aux(self, other):
        ''' Override this method instead of equals(). '''
        return self is other

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

    def free_vars(self, free_var_set):
        pass

    def match(self, other, env):
        if self == other:
            return env
        return None
    
    def show(self, stream):
        print(f"OBJECT({type(self)}", file=stream, end='')

    def __repr__(self):
        stream = io.StringIO()
        self.show(stream)
        return stream.getvalue()

    def __str__(self):
        stream = io.StringIO()
        self.disp(stream)
        return stream.getvalue()

    def type_name(self):
        raise Exception(f"Subclass {self.__class__.__name__} must implement Object.type_name")
