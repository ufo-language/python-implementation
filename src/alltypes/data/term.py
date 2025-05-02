from alltypes.data.array import Array
from alltypes.data.binding import Binding
from alltypes.data.hashtable import HashTable
from alltypes.expr.identifier import Identifier
from alltypes.literal.nil import Nil
from alltypes.literal.symbol import Symbol
from alltypes.object import Object
from alltypes.data._show_elems import show_elems

class Term (Object):

    __slots__ = ('_name', '_args', '_attrib')

    def __init__(self, name, args=None, attrib=None):
        self._name = name
        if args is None:
            args = Array()
        self._args = args
        self._attrib = Nil() if attrib is None else attrib

    @staticmethod
    def create(symbol_str, **kwargs):
        args_hash = HashTable()
        term = Term(Symbol(symbol_str), args_hash)
        for (name, value) in kwargs.items():
            args_hash[Identifier(name)] = value
        return term

    @staticmethod
    def from_parser(parse_value):
        return Term(*parse_value)

    def eval_rec(self, etor):
        name_value = etor.eval(self._name)
        args_value = self._args.eval(etor)
        # Attempt to create a hash table from the args (if they're all Bindings)
        hash = HashTable()
        is_hash = True
        for arg in args_value:
            if type(arg) is not Binding:
                is_hash = False
                break
            hash[arg.lhs()] = arg.rhs()
        if is_hash:
            args_value = hash
        attrib_value = etor.eval(self._attrib)
        return Term(name_value, args_value, attrib_value)
    
    def __getitem__(self, index):
        return self._args.get(index)
    
    def __setitem__(self, index, value):
        self._args[index] = value
    
    # use __getitem__ instead
    # def get(self, index):
    #     # return Array.get_with_elems(self, self._array._elems, index)
    #     return self._args.get(index)
    
    def get_attrib(self):
        return self._attrib

    def match(self, other, env):
        assert False

    def name(self):
        return self._name

    def parts(self):
        return Term.create(self.type_name(),
                           name=self._name,
                           args=self._args,
                           attrib=self._attrib)
    
    def set_attrib(self, attrib):
        self._attrib = attrib

    def show(self, stream):
        self._name.show(stream)
        self._args.show_with(stream, '{', ', ', '}')

    def type_name(self):
        return 'Term'
