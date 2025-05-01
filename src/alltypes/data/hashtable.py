from alltypes.data.binding import Binding
from alltypes.data._show_elems import show_elems
from alltypes.object import Object
from ufo_exception import UFOException

class HashTable (Object):
    
    class ProtoHash (Object):
        
        __slots__ = ('_bindings')

        def __init__(self, bindings):
            self._bindings = bindings

        @staticmethod
        def from_parser(parse_value):
            return HashTable.ProtoHash(parse_value)

        def bool_value(self):
            return len(self._bindings) > 0
        
        def eval_rec(self, etor):
            hash_table = HashTable()
            for binding_expr in self._bindings:
                binding_value = binding_expr.eval(etor)
                if type(binding_value) is not Binding:
                    raise UFOException("HashTable elements must be bindings", elem=binding_value)
                lhs = binding_value.lhs()
                rhs = binding_value.rhs()
                hash_table[lhs] = rhs
            return hash_table
        
        def type_name(self):
            return 'ProtoHash'

        def show(self, stream):
            stream.write('#{')
            first_iter = True
            for binding in self._bindings:
                if first_iter:
                    first_iter = False
                else:
                    stream.write(', ')
                binding.show(stream)
            stream.write('}')

    __slots__ = ('_hash',)

    def __init__(self):
        self._hash = {}

    # @staticmethod
    # def from_parser(parse_value):
    #     elems = parse_value
    #     hash_table = HashTable()
    #     for elem in elems:
    #         if not isinstance(elem, Binding):
    #             # This should never happen as long as the parser does its job.
    #             raise Exception(f"HashTable expected Binding, found {elem} :: {elem.type_name()}")
    #         hash_table[elem.lhs()] = elem.rhs()
    #     return hash_table

    def bool_value(self):
        return len(self._hash) > 0

    def eval_rec(self, etor):
        hash = HashTable()
        for (key, value) in self._hash.items():
            key_value = etor.eval(key)
            #print("HashTable.eval_rec key_value =", key_value)
            value_value = etor.eval(value)
            #print("HashTable.eval_rec value_value =", value_value)
            hash[key_value] = value_value
        return hash

    def __getitem__(self, key):
        return self._hash[key]

    def __setitem__(self, key, value):
        self._hash[key] = value

    def type_name(self):
        return 'HashTable'

    def show(self, stream):
        stream.write('#{')
        keys = sorted(self._hash.keys())
        first_iter = True
        for key in keys:
            if first_iter:
                first_iter = False
            else:
                stream.write(', ')
            key.show(stream)
            stream.write(Binding.CHAR)
            value = self._hash[key]
            value.show(stream)
        stream.write('}')
