import io

from ufo_exception import UFOException

class Object:

    __slots__ = ()

    def apply(self, args, etor):
        raise UFOException("Object is not applyable", object=self, type=self.type_name())

    def bool_value(self):
        return True
    
    def closure(self, env):
        return self

    def construct(self, term):
        print("Object.construct is not implemented")
        return None
    
    def count(self):
        raise UFOException("Object is uncountable", object=self, type=self.type_name())

    def display(self, stream):
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
        assert False

    def eval_compile(self, etor):
        assert False

    def free_vars(self, free_var_set):
        pass
    
    def get(self, index):
        raise UFOException("Object is not indexable", object=self, object_type=self.type_name(), index=index, index_type=index.type_name())

    def is_macro(self):
        return False

    def match(self, other, env):
        return self == other
    
    def parts(self):
        raise SystemError(f"parts is not implemented for type {type(self)}")

    def show(self, stream):
        print(f"OBJECT({type(self)}", file=stream, end='')

    def __repr__(self):
        stream = io.StringIO()
        self.show(stream)
        return stream.getvalue()

    def __str__(self):
        stream = io.StringIO()
        self.display(stream)
        return stream.getvalue()

    def type_name(self):
        raise Exception(f"Subclass {self.__class__.__name__} must implement Object.type_name")
